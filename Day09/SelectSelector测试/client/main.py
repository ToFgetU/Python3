#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Coosh
"""
简单的客户端
使用方法：put filename
测试并发：准备好一个几M文件，一个几十M文件，先put大的，再put小的，就能看到效果，也可以查看日志log.txt
待优化：只实现了上传
由于实在太简单了，我都懒得写注释了
"""
import os, sys, datetime
import socket

host = 'localhost'
port = 1234
sk = socket.socket()
sk.connect((host, port))
raw_input = input(">>>")
action = raw_input.split(maxsplit=1)[0]
filename = raw_input.split(maxsplit=1)[1]
filesize = os.stat(filename).st_size
print(filesize)
cmd = "%s|%s|%d" % (action, filename, filesize)
cmd = cmd.strip()
if cmd:
    sk.send(cmd.encode('utf8'))
    resp = sk.recv(1)
    buffer_size = 4096
    sent_size = 0
    with open(filename, 'rb') as fp:
        while fp.tell() < filesize:
            buffer = fp.read(buffer_size)
            sk.send(buffer)
            sent_size += len(buffer)
            print("已发送%d%%，%d字节" % (int(sent_size/filesize*100), sent_size))
    print("发送完毕")
sk.close()
