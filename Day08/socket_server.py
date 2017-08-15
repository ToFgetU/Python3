#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket

# 创建socket 连接
server = socket.socket()
conn = server.bind(('localhost', 10021))
server.listen()

while True:
    print("server start to listen")
    conn, addr = server.accept()
    while True:
        recv_data = conn.recv(1024).decode()
        print(recv_data)
        if recv_data == '再见':
            break
        send_data = input(">>> ").strip()
        conn.send(send_data.encode())
        if send_data == '再见':
            server.close()
            exit('退出程序')

