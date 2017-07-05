#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import selectors
import json
import os
from conf import settings
from core.ftpserver import SelectFtpServer

sel = selectors.DefaultSelector()

def accept(sock, mask):
    '''服务器连接'''
    conn, addr = sock.accept()
    # print('--------------->', self.conn, self.addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    '''程序执行'''
    try:
        data = conn.recv(1024)
        data = json.loads(data.decode())
        print(data)
        if data:
            if hasattr(SelectFtpServer, '_%s' % data.get('action')):
                func = getattr(SelectFtpServer, '_%s' % data.get('action'))
                func(SelectFtpServer, data, conn)
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
        for key, mask in events:
            print(key, mask)
            callback = key.data
            callback(key.fileobj, mask)




