#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket

sock = socket.socket()
sock.connect(('localhost', 10021))

while True:
    choice = input(">>> ").strip()
    if len(choice) == 0:
        continue
    sock.send(choice.encode())
    recv = sock.recv(1024)
    print('recv: ', recv.decode())