#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import json
import optparse
import os

class FTPClient(object):
    def __init__(self):
        self.parse = optparse.OptionParser()
        self.parse.add_option("-s", "--server", dest="server", help="ftp server ip addr")
        self.parse.add_option("-P", "--Port", type='int', dest="port", help="ftp server port")
        self.parse.add_option("-u", "--username", dest="username", help="ftp server user")
        self.parse.add_option("-p", "--password", dest="password", help="ftp server password")
        (self.opstions, self.args) = self.parse.parse_args()

        self.conn = self.make_connection()


    def make_connection(self):
        '''连接FTP服务端'''
        if self.opstions.server is None or self.opstions.port is None:
            self.parse.print_help()
            return False
        else:
            # print(self.opstions, self.args)
            self.client = socket.socket()
            self.client.connect((self.opstions.server, int(self.opstions.port)))
            return True

    def get_response(self):
        '''获取服务端返回数据'''
        data = self.client.recv(1024).strip()
        # print('recv data: ', data)
        data = json.loads(data.decode())
        return data

    def get_auth_resulet(self, username, password):
        '''获取服务端返回结果'''
        data_hander = {
            'action': 'auth',
            'username': username,
            'password': password
        }
        # print(data_hander)
        self.client.send(json.dumps(data_hander).encode())

        response = self.get_response()
        if response.get('status_code') == 200:
            self.user = username
            return True
        else:
            print(response.get('status_msg'))

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
                    print("Passed authentication!")
                    return self.get_auth_resulet(username, password)
                else:
                    retry_count += 1
            else:
                exit("输入超过三次")

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
        '''上传文件到服务器'''
        # print(*args, **kwargs)
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        file_path = cmd_list[1]
        filename = cmd_list[1].split("/")[-1]
        if os.path.isfile(cmd_list[1]):
            file_obj = open(file_path, 'rb')
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
        self.client.recv(1)  # 等待服务端确认
        self.client.send(file_obj.read())
        file_obj.close()
        self.client.recv(1)  # 确认接收完毕
        response = self.get_response()
        if response['status_code'] == 200:
            print("文件上传成功")
        else:
            print(response['status_msg'])

    def _get(self, cmd_list):
        '''服务端下载文件'''
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        filename = cmd_list[1]

        data_hander = {
            'action': cmd_list[0],
            'filename': filename
        }
        if self.__md5(cmd_list):
            data_hander = {
                'action': cmd_list[0],
                'filename': filename,
                'md5': 'md5'
            }
        self.client.send(json.dumps(data_hander).encode())
        response = self.get_response()
        # print(response)
        if response['status_code'] == 200:
            # self.client.send(b'1')  # 客户端确认可接收数据
            file_obj = open(response['filename'], 'wb')
            received_size = 0
            if self.__md5(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(response['size'])
                progress.__next__()
                while received_size < response['size']:
                    recv_data = self.client.recv(4096)
                    received_size += len(recv_data)
                    try:
                        progress.send(len(recv_data))
                    except Exception as e:
                        print('100%')
                    file_obj.write(recv_data)
                    md5_obj.update(recv_data)
                    # print(response['size'], received_size)
                else:
                    file_obj.close()
                    # self.client.send(b'1')  # 告诉服务端接收完毕
                    md5_val = md5_obj.hexdigest()
                    # print('md5_val', md5_val)
                    md5_response = self.get_response()
                    # print(md5_response)
                    if md5_response['status_code'] == 200:
                        if md5_val == md5_response['md5']:
                            print("文件校验一致，下载成功")
                        else:
                            print('文件下载异常，校验不一致')
                    else:
                        print(md5_response['status_msg'])
            else:
                progress = self.show_progress(response['size'])
                progress.__next__()
                received_size = 0
                while received_size < response['size']:
                    recv_data = self.client.recv(4096)
                    received_size += len(recv_data)
                    try:
                        progress.send(len(recv_data))
                    except Exception as e:
                        print('100%')
                    file_obj.write(recv_data)
                    # print(response['size'], received_size)
                else:
                    file_obj.close()
                    # self.client.send(b'1')  # 告诉服务端接收完毕
                    response = self.get_response()
                    # print(md5_response)
                    if response['status_code'] == 200:
                        print("文件下载成功")
                    else:
                        print(response['status_msg'])
        else:
            print(response['status_msg'])

if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()  # 交互
