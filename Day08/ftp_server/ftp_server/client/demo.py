#!/usr/bin/env python
# _*_ coding:utf-8_*_
import socket
server = socket.socket()
server.connect(('127.0.0.1',9999))
server.send('name'.encode())
print(server.recv(1024))
server.send('name'.encode())
print(server.recv(1024).decode())