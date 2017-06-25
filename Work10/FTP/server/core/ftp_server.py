#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socketserver
import json, os
import configparser
import hashlib
from conf import settings


STATUS_CODE = {
    200: 'Success',
    201: 'Invalid cmd',
    202: "Invalid cmd format. e.g: {'action':'get','filename':'test.py','size':344}",
    203: 'User or password is not correct',
    204: 'Invalid filename',
    205: 'Invalid path',
    206: 'Insufficient disk space',
    207: 'The File has been downloaded'
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
        print('__', *args, **kwargs)
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
                self.path_name = "%s/%s" % (settings.USER_HOME, self.user)
                self.change_path = ''
                return self.send_response(200)
            else:
                return self.send_response(203)

    def _put(self, *args, **kwargs):
        '''上传到服务器'''
        data = args[0]
        print('data ', data)
        user_home = "%s/%s" % (settings.USER_HOME, self.user)
        if data['filename'] is not None:
            # 转换成字节数
            config = configparser.ConfigParser()
            config.read(settings.ACCOUNT_FILE)
            if config.has_section(self.user):
                config_size = float(config[self.user]['Quotation']) * 1024 * 1024
                used_size = float(config[self.user]['Used']) * 1024 * 1024
                total_size = used_size + data['size']
                if total_size > config_size:
                    self.send_response(206)
                else:
                    self.request.send(b'1')  # 服务端端确认可接收数据
                    file_obj = open('%s/%s' % (user_home, data['filename']), 'wb')
                    received_size = 0
                    while received_size < data['size']:
                        recv_data = self.request.recv(4096)
                        file_obj.write(recv_data)
                        received_size += len(recv_data)
                        # print(data['size'], received_size)
                    else:
                        file_obj.close()
                        config.set(self.user, 'Used', str(total_size/1024/1024))
                        config.write(open(settings.ACCOUNT_FILE, 'w'))
                        self.request.send(b'1')  # 告诉服务端接收完毕
                        self.send_response(200)
                        print("文件接收完毕")
            else:
                self.send_response(201)


    def _get(self, *args, **kwargs):
        data = args[0]
        print('data', data)
        user_home = "%s/%s" % (settings.USER_HOME, self.user)
        filename = '%s/%s' % (user_home, data['filename'])

        if os.path.getsize('%s/%s' % (user_home, data['filename'])) == data['down_size']:
            self.send_response(207)
        else:
            if os.path.exists(filename):
                file_obj = open(filename, 'rb')
                file_obj.seek(data['down_size'], 0)
                data_hander = {
                    'filename': data['filename'],
                    'size': os.path.getsize('%s/%s' % (user_home, data['filename']))
                }
                self.send_response(200, data=data_hander)
                self.request.recv(1) # 等待客户端确认

                if data.get('md5'):
                    md5_obj = hashlib.md5()
                    for line in file_obj:
                        self.request.send(line)
                        md5_obj.update(line)
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()

                    self.request.recv(1) # 确认接收完毕
                    self.send_response(200, {'md5': md5_val})
                    print("文件传输成功")
                else:
                    for line in file_obj:
                        self.request.send(line)
                    file_obj.close()

                    self.request.recv(1)  # 确认接收完毕
                    self.send_response(200)
                    print("文件传输成功")
            else:
                self.send_response(204)

    def _ls(self, *args, **kwargs):
        '''显示列表'''
        data = args[0]
        print('data', data)
        # user_home = "%s/%s" % (settings.USER_HOME, self.user)
        if os.path.exists(self.path_name):
            file_list = os.listdir(self.path_name)
        else:
            file_list = os.listdir(user_home)
        data_hander = {
            'file_list': file_list
        }
        self.send_response(200, data=data_hander)
        self.request.recv(1)

    def _cd(self, *args, **kwargs):
        '''目录选择'''
        data = args[0]
        print(data)
        user_home = "%s" % (settings.USER_HOME)
        if data['path'] is not None:
            if data['path'] == '~':
                path_name = "%s/%s" % (settings.USER_HOME, self.user)
            elif data['path'] == '..':
                path_name = os.path.dirname(self.path_name)
            else:
                path_name = '%s/%s' % (self.path_name, data['path'])
            if user_home not in self.path_name or user_home == path_name:
                self.send_response(205)
                return
            if os.path.exists(path_name):
                data_hander = {
                    'path': path_name
                }
                self.path_name = path_name
                self.send_response(200, data=data_hander)
                self.request.recv(1)
            else:
                self.send_response(205)
        else:
            self.send_response(205)


    def _pwd(self, *args, **kwargs):
        '''查看当前目录'''
        data = args[0]
        print(data)
        if self.path_name:
            data_hander = {
                'path': self.path_name
            }
            self.send_response(200, data=data_hander)
        else:
            self.send_response(201)

