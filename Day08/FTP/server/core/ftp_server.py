#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socketserver
import json, os
import configparser
from conf import settings


STATUS_CODE = {
    200: 'Success',
    201: 'Invalid cmd',
    202: "Invalid cmd format. e.g: {'action':'get','filename':'test.py','size':344}",
    203: 'User or password is not correct'

}

class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.data)
            print(self.client_address)

            if not self.data:
                print("client [%s] closed" % self.client_address[0])
                break
            data = json.loads(self.data.decode())
            if data.get('action'):
                if hasattr(self, '_%s' % data.get('action')):
                    func = getattr(self, '_%s' % data.get('action'))
                    func(data)
                else:
                    self.send_response(201)
            else:
                self.send_response(200)

    def send_response(self, status_code, data=None):
        '''向客户端返回数据信息'''
        response = {
            'status_code': status_code,
            'status_msg': STATUS_CODE[status_code]
        }
        if data:
            response.update(data)
        print('------->', response)
        self.request.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        '''验证用户并创建用户家目录'''
        print(*args, **kwargs)
        data = args[0]
        if data.get('username') is None or data.get('password') is None:
            self.send_response(203)

        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)

        if data.get('username') in config.sections():
            _password = config[data.get('username')]['Password']
            if _password == data.get('password'):
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
        user_home = "%s/%s" % (settings.USER_HOME, self.user)
        if data['filename'] is not None:
            file_obj = open('%s/%s' % (user_home, data['filename']), 'wb')
            while True:
                received_size = 0
                while received_size < args:
                    recv_data = self.request.recv(4096)
                    file_obj.write(recv_data)
                    received_size += len(recv_data)
                else:
                    file_obj.close()
                    self.send_response(200)


