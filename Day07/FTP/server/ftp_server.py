#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import json

sock = socket.socket()

sock.bind(('localhost', 10021))

sock.listen(5)

while True:
    conn, client_addr = sock.accept()
    print("got a new conn:", client_addr)

    while True:
        data = conn.recv(1024)
        print("recv data: ", data)

        data = json.loads(data.decode())

        if data.get('action') is not None:
            if data['action'] == 'put':
                file_obj = open(data['filename'], 'wb')
                revc_size = 0

                while revc_size < data['size']:
                    recv_data = conn.recv(4096)
                    file_obj.write(recv_data)
                    revc_size += len(recv_data)
                    print(data['size'], revc_size)
                else:
                    print("successfully received file")
                    file_obj.close()
            elif data['action'] == 'get':
                pass