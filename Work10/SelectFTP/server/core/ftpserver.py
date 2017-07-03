#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import selectors
import json
import os
from conf import settings

STATUS_CODE = {
    200: 'Success',
    201: 'Invalid cmd',
    202: "Invalid cmd format. e.g: {'action':'get','filename':'test.py','size':344}",
    203: 'User or password is not correct',
    204: 'Invalid filename'

}

class SelectFtpServer(object):
    '''select FTP server 服务器'''
    sel = selectors.DefaultSelector()

    def start(self):
        '''启动程序入口'''
        self.sock = socket.socket()
        self.sock.bind(settings.host_port)
        self.sock.listen(10)
        self.sock.setblocking(False)
        SelectFtpServer.sel.register(self.sock, selectors.EVENT_READ, self.accept)

        while True:
            events = SelectFtpServer.sel.select()
            for key, mask in events:
                print(key, mask)
                callback = key.data
                callback(mask)

    def accept(self, mask):
        '''服务器连接'''
        self.conn, self.addr = self.sock.accept()
        # print(self.conn, self.addr)
        self.conn.setblocking(False)
        SelectFtpServer.sel.register(self.conn, selectors.EVENT_READ, self.read)

    def read(self, mask):
        '''程序执行'''
        self.data = self.conn.recv(1024)
        data = json.loads(self.data.decode())
        if data:
            if hasattr(self, '_%s' % data.get('action')):
                func = getattr(self, '_%s' % data.get('action'))
                func(data)
            else:
                exit('Invalid cmd')
        else:
            print('closing', self.conn)
            SelectFtpServer.sel.unregister(self.conn)
            self.conn.close()

    def send_response(self, status_code, data=None):
        '''向客户端返回数据信息'''
        response = {
            'status_code': status_code,
            'status_msg': STATUS_CODE[status_code]
        }
        if data:
            response.update(data)
        print('------->', response)
        self.conn.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        print('args', args)
        data = args[0]
        if data.get('username') in settings.user_dict:
            if data.get('password') == settings.user_dict[data.get('username')]:
                self.user = data.get('username')
                if os.path.exists("%s/%s" % (settings.USER_HOME, self.user)):
                    pass
                else:
                    os.makedirs("%s/%s" % (settings.USER_HOME, self.user))
                return self.send_response(200)
        else:
            return self.send_response(203)

    def _put(self, *args, **kwargs):
        '''上传到服务器'''
        data = args[0]
        print('data', data)
        # data_hander = {
        #     'data': data
        # }
        # self.send_response(200, data=data_hander)
        user_home = "%s/%s" % (settings.USER_HOME, self.user)
        if data['filename'] is not None:
            self.conn.send(b'1')  # 服务端端确认可接收数据
            file_obj = open('%s/%s' % (user_home, data['filename']), 'wb')
            received_size = 0
            while received_size < data['size']:
                recv_data = self.conn.recv(4096)
                file_obj.write(recv_data)
                received_size += len(recv_data)
                print(data['size'], received_size)
            else:
                file_obj.close()
                self.conn.send(b'1')  # 告诉服务端接收完毕
                self.send_response(200)
                print("文件接收完毕")

    def _get(self):
        data = args[0]
        print('data', data)
        user_home = "%s/%s" % (settings.USER_HOME, self.user)
        filename = '%s/%s' % (user_home, data['filename'])
        if os.path.exists(filename):
            file_obj = open(filename, 'rb')
            data_hander = {
                'filename': data['filename'],
                'size': os.path.getsize('%s/%s' % (user_home, data['filename']))
            }
            self.send_response(200, data=data_hander)
            # self.conn.recv(1)  # 等待客户端确认

            for line in file_obj:
                self.conn.send(line)
            file_obj.close()

            # self.conn.recv(1)  # 确认接收完毕
            self.send_response(200)
            print("文件传输成功")
        else:
            self.send_response(204)


