#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Coosh
"""
SELECT版超级简单版服务器端
"""
import os, sys, datetime, time
import selectors
import socket
from conf import settings


sel = selectors.SelectSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

upload_jobs = dict()   # 上传的任务，写成一个字典存放，以链接为key
download_jobs = dict()   # 下载的任务，写成一个字典存放
def read(conn, mask):
    try:
        data = conn.recv(4096)
        print(data)
        if data:
            if data.startswith(b"auth"):
                username = data.split(b'|')[1].decode()
                password = data.split(b'|')[2].decode()
                # print(username, password)
                if username in settings.user_dict:
                    if password == settings.user_dict[username]:
                        conn.send(b'1') # 用户登入成功确认
                        print('用户登入成功')
                        # 判断创建家目录
                        if os.path.exists("%s/%s" % (settings.USER_HOME, username)):
                            pass
                        else:
                            os.makedirs("%s/%s" % (settings.USER_HOME, username))
                    else:
                        print('用户密码错误')
                        conn.send(b'0')
                else:
                    print('用户密码错误')
                    conn.send(b'0')
            if data.startswith(b"put") and data.split(b'|')[0] == b'put': #二进制文件可能刚好发送了put开头的二进制字符串，所以再用条件限制下
                print('获取put请求')
                filename = (data.split(b'|')[1].decode())
                # filename = filename.split('/')[-1]
                filesize = int(data.split(b'|')[3].decode())
                username = data.split(b'|')[2].decode()
                # p_filename = "%s/%s/%s" % (settings.USER_HOME, username, filename)
                # print(settings.USER_HOME, username, filename)
                p_filename = os.path.join(settings.USER_HOME, username, filename)
                # print(p_filename)
                if os.path.exists(p_filename) and os.path.getsize(p_filename) == filesize:
                    conn.send(b'0')
                else:
                    upload_jobs[conn] = dict(filename=filename, filesize=filesize, received_size=0, fp=open(p_filename, 'ab'))
                    conn.send(b'1')
            elif data.startswith(b"get") and data.split(b'|')[0] == b'get':
                print('获取get请求')
                filename = data.split(b'|')[1].decode() # 接受到的命令格式应该为get|filename
                username = data.split(b'|')[2].decode()
                # print((settings.USER_HOME, username, filename))
                # g_filename = "%s/%s/%s" % (settings.USER_HOME, username, filename)
                g_filename = os.path.join(settings.USER_HOME, username, filename)
                print(g_filename)
                if os.path.exists(g_filename):
                    filesize = os.stat(g_filename).st_size
                    s_cmd = '%s|%s' % (filename, filesize)
                    print(s_cmd)
                    download_jobs[conn] = dict(filename=filename, filesize=filesize, sent_size=0, fp=open(g_filename, 'rb'))
                    conn.send(s_cmd.encode('utf8'))
                else:
                    conn.send(b'0')
            else:
                if conn in upload_jobs:
                    print('开始上传')
                    fp = upload_jobs[conn]['fp']
                    remain_size = upload_jobs[conn]['filesize'] - upload_jobs[conn]['received_size']  # 获得余下文件数据的长度
                    if remain_size <= 4096:
                        # 接收剩余的字节
                        data = data[:remain_size]
                        fp.write(data)
                        fp.flush()
                        print('已接收', upload_jobs[conn]['received_size'])
                        fp.close()
                        del upload_jobs[conn]
                    else:
                        fp.write(data)
                        fp.flush()
                        upload_jobs[conn]['received_size'] += len(data)  #
                        print('已接收', upload_jobs[conn]['received_size'])
                elif conn in download_jobs:
                    # if data.decode() == b'1':
                    #     pass
                    print('进入下载')
                    data = data.decode()
                    print(data)
                    sent_size = int(data.split('|')[1])
                    fp = download_jobs[conn]['fp']
                    # print(fp.tell())
                    print('已下载', sent_size, download_jobs[conn]['filesize'])
                    fp.seek(sent_size, 0)
                    buffer_size = 4096
                    if fp.tell() < download_jobs[conn]['filesize']:
                        buffer = fp.read(buffer_size)
                        print(buffer)
                        conn.send(buffer)
                        # fp.close()
                    else:
                        fp.close()
                        del download_jobs[conn]
        else:
            print('closing', conn)
            sel.unregister(conn)
            conn.close()
    except ConnectionResetError:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

def start():
    '''启动程序入口'''
    sock = socket.socket()
    sock.bind(settings.host_port)
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)
    print('FTP服务启动'.center(60, '='))

    while True:
        events = sel.select()
        print('事件触发')
        for key, mask in events:
            # print(key, mask)
            callback = key.data
            callback(key.fileobj, mask)


