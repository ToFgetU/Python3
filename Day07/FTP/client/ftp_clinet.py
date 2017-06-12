#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import os
import json

sock = socket.socket()
sock.connect(('localhost', 10021))

while True:
    choice = input(">>> ").strip()
    if len(choice) == 0:
        continue
    cmd_list = choice.split()
    if cmd_list[0] == 'put':
        if len(cmd_list) == 1:
            print("no filename follows after put cmd")
            continue
        filename = cmd_list[1]
        # os.path.split(cmd_list[1]) # 获取路径和文件
        if os.path.isfile(filename):
            file_obj = open(filename, 'rb')
            base_filename = filename.split("/")[-1]
            print(base_filename, os.path.getsize(filename))
            data_header = {
                'action': 'put',
                'filename': base_filename,
                'size': os.path.getsize(filename)
            }
            sock.send(json.dumps(data_header).encode())
            for line in file_obj:
                sock.send(line)
            print("send over")
            file_obj.close()
        else:
            print("file is not valid")
            continue

    elif cmd_list[0] == 'get':
        pass