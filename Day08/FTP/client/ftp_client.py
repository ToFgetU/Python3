#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import optparse
import json, os

STATUS_CODE = {
    200: 'Success',
    201: 'Invalid cmd',
    202: 'User or password is not correct'

}

class FTPClient(object):
    '''FTP客户端'''
    def __init__(self):
        self.parse = optparse.OptionParser()
        self.parse.add_option("-s", "--server", dest="server", help="ftp server ip addr")
        self.parse.add_option("-P", "--Port", type='int', dest="port", help="ftp server port")
        self.parse.add_option("-u", "--username", dest="username", help="ftp server user")
        self.parse.add_option("-p", "--password", dest="password", help="ftp server password")
        (self.opstions, self.args) = self.parse.parse_args()

        self.conn = self.make_connection()
        # self.authenticate()

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

    def get_auth_resulet(self, username, password):
        '''获取服务端返回结果'''
        data_hander = {
            'action': 'auth',
            'username': username,
            'password': password
        }
        print(data_hander)
        self.client.send(json.dumps(data_hander).encode())

        response = self.get_response()
        if response.get('status_code') == 200:
            print("Passed authentication!")
            self.user = username
            return True
        else:
            print(response.get('status_msg'))


    def get_response(self):
        '''获取服务端返回数据'''
        data = self.client.recv(1024).strip()
        print('recv data: ', data)
        data = json.loads(data.decode())
        return data


    def authenticate(self):
        '''验证用户参数'''
        if self.conn:
            pass
        else:
            exit()
        if self.opstions.username is None and self.opstions.password is not None:
            exit("Err: 没有输入用户")
        elif self.opstions.username is not None and self.opstions.password is None:
            password = input("password: ").strip()
            return self.get_auth_resulet(self.opstions.username, password)
        elif self.opstions.username is None and self.opstions.password is None:
            retry_count = 0
            while retry_count < 3:
                username = input("username: ").strip()
                password = input("password: ").strip()
                if self.get_auth_resulet(username, password):
                    return self.get_auth_resulet(username, password)
                else:
                    retry_count += 1

        else:
            return self.get_auth_resulet(self.opstions.username, self.opstions.password)



    def interactive(self):
        '''FTP交互'''
        if self.authenticate():
            print("开始交互")
            while True:
                choice = input('[%s] >>> ' % self.user).strip()
                if len(choice) == 0:
                    continue
                cmd_list = choice.split()
                if hasattr(self, '_%s' % cmd_list[0]):
                    func = getattr(self, '_%s' % cmd_list[0])
                    func(cmd_list)
                else:
                    print("Invalid cmd.")

    def _put(self, cmd_list):
        '''上传到服务器'''
        # print(*args, **kwargs)
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        filename = cmd_list[1].split("/")[-1]
        if os.path.isfile(cmd_list[1]):
            pass
        else:
            print("%s is not a file or file is not exit..." % filename)
            return
        data_hander = {
            'action': cmd_list[0],
            'filename': filename,
            'size': os.path.getsize(cmd_list[1])
        }

        self.client.send(json.dumps(data_hander).encode())
        response = self.get_response()
        print(response)







if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive() #交互

