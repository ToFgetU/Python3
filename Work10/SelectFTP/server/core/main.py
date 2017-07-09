#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import selectors
import json
import os
from conf import settings
from core.ftpserver import SelectFtpServer
import threading, time

sel = selectors.DefaultSelector()

def accept(sock, mask):
    '''服务器连接'''
    conn, addr = sock.accept()
    # print('--------------->', self.conn, self.addr)
    print('accepted', conn, 'from', addr, '--mask', mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

upload_dict = dict()
download_dict = dict()
def read(conn, mask):
    '''程序执行'''
    print('开始')
    try:
        data = conn.recv(4096)
        data = json.loads(data.decode())
        print(data)
        if data:
            if hasattr(SelectFtpServer, '_%s' % data.get('action')):
                func = getattr(SelectFtpServer, '_%s' % data.get('action'))
                # t = threading.Thread(target=func, args=(SelectFtpServer, data, conn))
                # t.start()
                if data.get('action') == 'auth':
                    func(SelectFtpServer, data, conn)
                elif data.get('action') == 'put':
                    filename = data['filename']  # 接受到的命令格式应该为put|filename|filesize
                    filesize = data['size']
                    upload_jobs[conn] = dict(action=func, filename=filename, filesize=filesize, received_size=0,
                                             fp=open(filename, mode='ab'))
                    conn.send(b'1')
                elif data.get('action') == 'get':
                    filename = data['filename']  # 接受到的命令格式应该为get|filename
                    filesize = data['size']
            elif conn in upload_dict:
                fp = upload_jobs[conn]['fp']
                remain_size = upload_jobs[conn]['filesize'] - upload_jobs[conn]['received_size']  # 获得余下文件数据的长度
                if remain_size <= 4096:  # 如果少于或等于4096个字节，代表这是最后一次读取
                    data = data[:remain_size]
                    fp.write(data)
                    fp.flush()
                    fp.close()
                    del upload_jobs[conn]  # 写入完毕后，从上传任务中移出该链接
                else:
                    # 余下超过4096个字节，则把读取到的data全部写入
                    fp.write(data)
                    fp.flush()
                    upload_jobs[conn]['received_size'] += len(data)  # 更新已接受的总大小
                msg = "收到来自%s，数据长度为%d字节" % (str(conn), len(data))
                print(msg)
            elif conn in download_dict:
                pass
            else:
                exit('Invalid cmd')
        else:
            print('closing', conn)
            sel.unregister(conn)
            conn.close()
    except Exception as e:
        print(e)
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
        res_list = []
        # time.sleep(10)
        for key, mask in events:
            # print(key, mask)
            callback = key.data
            callback(key.fileobj, mask)
        #     t = threading.Thread(target=callback, args=(key.fileobj, mask))
        #     t.start()
        #     res_list.append(t)
        # for j in res_list:
        #     j.join()




