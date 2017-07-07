#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Coosh
"""
SELECT版超级简单版服务器端
目前只实现了上传，参考read()函数
使用方法：直接执行即可
待优化：未对断线的客户端进行处理，比如断线后fp未关闭
"""
import os, sys, datetime, time
import selectors
import socket

sel = selectors.SelectSelector()
log_flag = True

# accept函数直接拷贝官方文档的，不是重点
def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def log(msg):
    if log_flag:
        with open("log.txt", "a", encoding="utf8") as f:
            f.write(msg + "\n")

# 关键代码↓
upload_jobs = dict()   # 上传的任务，写成一个字典存放，以链接为key
download_jobs = dict()   # 下载的任务，写成一个字典存放
def read(conn, mask):
    try:
        data = conn.recv(4096)  # Should be ready
        if data:    # 有数据
            if data.startswith(b"put"):
                # 当这个数据是一条上传指令，则进行以下初始化任务
                filename = data.split(b"|")[1]   # 接受到的命令格式应该为put|filename|filesize
                filesize = int(data.split(b"|")[2])
                upload_jobs[conn] = dict(filename=filename, filesize=filesize, received_size=0, fp=open(filename, mode='ab'))
                conn.send(b'1')
            elif data.startswith(b"get"):
                # 下载指令，初始化任务
                pass
            else:
                if conn in upload_jobs:
                    # 如果本链接是上传任务
                    fp = upload_jobs[conn]['fp']
                    remain_size = upload_jobs[conn]['filesize'] - upload_jobs[conn]['received_size']    # 获得余下文件数据的长度
                    if remain_size <= 4096:  # 如果少于或等于4096个字节，代表这是最后一次读取
                        data = data[:remain_size]
                        fp.write(data)
                        fp.flush()
                        fp.close()
                        del upload_jobs[conn]   # 写入完毕后，从上传任务中移出该链接
                    else:
                        # 余下超过4096个字节，则把读取到的data全部写入
                        fp.write(data)
                        fp.flush()
                        upload_jobs[conn]['received_size'] += len(data) # 更新已接受的总大小
                    msg = "收到来自%s，数据长度为%d字节" % (str(conn), len(data))
                    log(msg)
                    print(msg)
                elif conn in download_jobs:
                    # 如果本链接是下载任务
                    pass
                else:
                    # 不知道这个链接是什么鬼，把收到的数据发还回去
                    conn.send(data)

        else:
            print('closing', conn)
            sel.unregister(conn)
            conn.close()
    except ConnectionResetError:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()
# 关键代码↑


# 以下代码不是重点，稍微看一下即可
host = 'localhost'
port = 1234
sock = socket.socket()
sock.bind((host, port))
sock.listen(100)
sock.setblocking(False)
print("开始侦听 %s:%d" % (host, port))
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
