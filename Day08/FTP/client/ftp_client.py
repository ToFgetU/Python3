#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import optparse
import json

class FTPClient(object):
    '''FTP客户端'''
    def __init__(self):
        self.parse = optparse.OptionParser()
        self.parse.add_option("-s", "--server", dest="server", help="ftp server ip addr")
        self.parse.add_option("-P", "--Port", type='int', dest="port", help="ftp server port")
        self.parse.add_option("-u", "--username", dest="username", help="ftp server user")
        self.parse.add_option("-p", "--password", dest="password", help="ftp server password")
        (self.opstions, self.args) = self.parse.parse_args()
        self.authenticate()
        self.make_connection()

    def make_connection(self):
        '''连接FTP服务端'''
        if self.opstions.server is None or self.opstions.port is None:
            self.parse.print_help()
            return False
        else:
            print(self.opstions, self.args)
            self.client = socket.socket()
            self.client.connect((self.opstions.server, int(self.opstions.port)))
            return True

    def authenticate(self):
        '''验证用户参数'''
        if self.opstions.username is None and self.opstions.password is not None:
            exit("Err: 没有输入用户")
        elif self.opstions.username is not None and self.opstions.password is None:
            password = input("password: ").strip()
            return get_auth_resulet(self.opstions.username, password)
        elif self.opstions.username is None and self.opstions.password is None:
            username = input("username: ").strip()
            password = input("password: ").strip()
            return get_auth_resulet(username, password)
        else:
            return get_auth_resulet(self.opstions.username, self.opstions.password)



    def get_auth_resulet(self, username, password):
        '''获取服务端返回结果'''
        data_hander = {
            'action': 'auth',
            'username': username,
            'password': password
        }
        print(data_hander)
        self.client.send(json.dumps(data_hander).encode())

        response = get_response()

    def get_response(self):
        pass


    def interactive(self):
        '''FTP交互'''
        # while True:
        pass




if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive() #交互

