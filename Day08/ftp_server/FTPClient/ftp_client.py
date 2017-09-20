#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import socket
import time
import selectors
server = socket.socket()
server.connect(('127.0.0.1',8888))
size = os.path.getsize('tmp/file.txt')


server.send(str(size).encode())
time.sleep(1)
with open('tmp/file.txt','rb') as f:
    # for i in f:
    #     server.send(i)
    buffer_size = 1024
    while f.tell() < size:
        buffer = f.read(buffer_size)
        server.send(buffer)
        print("-->", buffer)

print(server.recv(1024).decode())


'''
data = input('>>>')
server.send(data.encode('utf8'))
print(server.recv(1024))
'''