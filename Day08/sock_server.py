#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import json
import os

sock = socket.socket()
sock.bind(('localhost', 10021))

sock.listen(5)

while True:
    conn, client_addr = sock.accept()
    print("got a new conn:", client_addr)
    while True:
        data = conn.recv(1024)
        print("recv data:", data)
        data = json.loads(data.decode())

        if data.get('action') is not None:
            if data['action'] == 'put':
                file_obj = open(data["filename"], 'wb')
                received_size = 0
                while received_size < data['size']:
                    recv_data = conn.recv(4096)
                    file_obj.write(recv_data)
                    received_size += len(recv_data)
                else:
                    file_obj.close()
                    print("Successfully received file [%s]" % data['filename'])
            elif data['action'] == 'get':
                filename = data['filename'].split('/')[-1]
                file_obj = open(filename, 'rb')
                data_header = {
                    'filename': filename,
                    'size': os.path.getsize(os.path.abspath(filename))
                }
                print(data_header)
                conn.send(json.dumps(data_header).encode())

                for line in file_obj:
                    conn.send(line)
                else:
                    print("send file down")
