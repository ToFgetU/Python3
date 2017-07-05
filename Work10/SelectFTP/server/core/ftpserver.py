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


    @staticmethod
    def send_response(status_code, conn, data=None):
        '''向客户端返回数据信息'''
        response = {
            'status_code': status_code,
            'status_msg': STATUS_CODE[status_code]
        }
        if data:
            response.update(data)
        print('------->', response)
        conn.send(json.dumps(response).encode())

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
                SelectFtpServer.send_response(200, args[1])
        else:
            SelectFtpServer.send_response(203, args[1])

    @staticmethod
    def _put(*args, **kwargs):
        '''上传到服务器'''
        data = args[1]
        print('data', data)
        print(args)
        user = data['username']
        print('user:', user)
        # data_hander = {
        #     'data': data
        # }
        # self.send_response(200, data=data_hander)
        user_home = "%s/%s" % (settings.USER_HOME, user)
        if data['filename'] is not None:
            args[2].send(b'1')  # 服务端端确认可接收数据
            file_obj = open('%s/%s' % (user_home, data['filename']), 'wb')
            received_size = 0
            while received_size < data['size']:
                # 由于是非阻塞性模式，所以当recv没接到数据时会出现异常，所以对其进行捕获并处理
                try:
                    recv_data = args[2].recv(4096)
                    file_obj.write(recv_data)
                    received_size += len(recv_data)
                    print(data['size'], received_size)
                except:
                    continue
            else:
                file_obj.close()
                args[2].send(b'1')  # 告诉服务端接收完毕
                SelectFtpServer.send_response(200, args[2])
                print("文件接收完毕")

    @staticmethod
    def _get(*args, **kwargs):
        data = args[1]
        print('data', data)
        user_home = "%s/%s" % (settings.USER_HOME, data['username'])
        filename = '%s/%s' % (user_home, data['filename'])
        if os.path.exists(filename):
            file_obj = open(filename, 'rb')
            data_hander = {
                'filename': data['filename'],
                'size': os.path.getsize('%s/%s' % (user_home, data['filename']))
            }
            SelectFtpServer.send_response(200, args[2], data=data_hander)
            while True:
                try:
                    t = args[2].recv(1)  # 等待客户端确认
                    print('t', t)
                    break
                except:
                    continue
            # for line in file_obj:
            #     args[2].send(line)
            f = file_obj.read()
            args[2].sendall(f)
            file_obj.close()

            while True:
                try:
                    t = args[2].recv(1)  # 确认接收完毕
                    print('t', t)
                    break
                except:
                    continue
            SelectFtpServer.send_response(200, args[2])
            print("文件传输成功")
        else:
            self.send_response(204, args[2])


