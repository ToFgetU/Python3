#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import json
import optparse

class FTPClient(object):
    '''FTP客户端实现'''
    def __init__(self):
        self.parse = optparse.OptionParser()
        self.parse.add_option("-s", "--server", dest="server", help="ftp server ip addr")
        self.parse.add_option("-P", "--Port", dest = "port", help="ftp server port")
        self.parse.add_option("-u", "--username", dest="username", help="username")
        self.parse.add_option("-p", "--password", dest="password", help="password")
        (self.options, self.args) = self.parse.parse_args()

        self.verify_args(options, args)
        self.make_connection()

    def verify_args(self, options, args):
        '''参数校验'''
        if options.username and options.password:
            pass
        elif options.username is not None and options.password is not None:
            pass
        else:
            exit("Err: 用户密码需要同时存在或不输入")

        if options.port > 0 and options.port < 65535:
            return True
        else:
            exit("Err: 端口号必须在 0 -65535")

    def make_connection(self):
        '''ftp连接'''
        self.sock = socket.socket()
        self.sock.connect((self.server, self.port))

    def get_auth_result(self, username, password):
        '''获取服务端返回用户验证结果'''
        data = {
            'action': 'auth',
            'username': username,
            'password': password
        }
        self.sock.send(json.dumps(data.encode()))
        response = get_response()

    def authenticate(self, username, password):
        '''验证用户'''
        if self.options.username:
            return get_auth_result(username, password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username: ").strip()
                password = input("password: ").strip()
                return get_auth_result(username, password)

    def get_response(self):
        data = self.sock.recv(1024).strip()
        print(data)



if __name__ == '__main__':
    ftp = FTPClient()