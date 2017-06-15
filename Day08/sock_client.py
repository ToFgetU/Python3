#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import os
import json

sock = socket.socket()
sock.connect(("localhost", 10021))

while True:
    choice = input((">>> ")).strip()
    if len(choice) == 0: continue

    cmd_list = choice.split()
    if len(cmd_list) == 1:
        print("no filename follows after put cmd")
        continue

    filename = cmd_list[1]
    if cmd_list[0] == 'put':
        if os.path.isfile(filename):
            file_obj = open(filename, 'rb')
            base_filename = filename.split('/')[-1]
            print(base_filename, os.path.getsize(filename))
            data_header = {
                'action': 'put',
                'filename': base_filename,
                'size': os.path.getsize(filename)
            }
            sock.send(json.dumps(data_header).encode())
            for line in file_obj:
                sock.send(line)

            print("send file done")

        else:
            print("is not file")
            continue
    elif cmd_list[0] == 'get':
        file_obj = open(filename, 'wb')
        data_header = {
            'action': 'get',
            'filename': filename
        }
        sock.send(json.dumps(data_header).encode())
        data = sock.recv(1024)
        data = json.loads(data.decode())
        print(data)
        recv_size = 0
        while recv_size < data['size']:
            recv_data = sock.recv(4096)
            file_obj.write(recv_data)
            recv_size += len(recv_data)
        else:
            file_obj.close()
            print("file get successfully")


