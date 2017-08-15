#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket

client = socket.socket()
client.connect(('localhost', 10021))

print("--> connect")
while True:
    send_data = input(">>> ").strip()
    client.send(send_data.encode())
    if send_data == '再见':
        client.close()
        exit("退出程序")
    elif send_data == '':
        continue
    else:
        recv_data = client.recv(1024).decode()
        if recv_data == '再见':
            client.close()
            exit('退出程序')
        print(recv_data)


