#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import optparse


STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
}

class FTPClient(object):
    def __init__(self):
        self.parse = optparse.OptionParser()
        self.parse.add_option('-s', '--host', dest='host', help='ftp server ip_addr')
        self.parse.add_option('-P', '--port', dest='port', help='ftp server port')
        self.parse.add_option('-u', '--username', dest='username', help='ftp server username')
        self.parse.add_option('-p', '--password', dest='password', help='ftp server password')
        (self.options, self.args) = self.parse.parse_args()
        self.verity_args(self.options, self.args)
        self.make_connection()

    def make_connection(self):
        try:
            self.sock = socket.socket()
            self.sock.connect((self.options.host, self.options.port))
        except Exception as e:
            print(e)
            self.parse.print_help()

    def verity_args(self, options, args):
        '''校验参数'''
        if options.username is not None and options.password is not None:
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            # 用户密码有一个为空
            exit("Err: 用户密码必须同时存在或者不输入")
        if options.host and options.port:
            if int(options.port) > 0 and int(options.port) < 65535:
                return True
            else:
                exit("Err: 端口必须在 0 - 65535 ")

    def authenticate(self):
        '''用户验证'''
        if self.options.username:
            print(self.options.username, self.options.password)
            return get_auth_result(username, password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username: ").strip()
                password = input("password: ").strip()
                return get_auth_result(username, password)

    def get_auth_result(self, username, password):
        data = {
            'action': 'auth',
            'username': username,
            'password': password
        }
        self.sock.send(json.dumps(data).encode())
        response = self.get_response()
        if response.get('status_code') == 254:
            print(STATUS_CODE[254])
            self.username = username
            return True
        else:
            print(response.get("status_msg"))

    def get_response(self):
        """获取服务器端回复"""
        data = self.sock.recv(1024)
        print("server recv: ", data)
        data = json.loads(data.decode())
        return data

    def interactive(self):
        if self.authenticate():
            print("---start interactive iwth u...")
            while True:
                choice = input("[%s]:" % self.user).strip()
                if len(choice) == 0: continue
                cmd_list = choice.split()
                if hasattr(self, "_%s" % cmd_list[0]):
                    func = getattr(self, "_%s" % cmd_list[0])
                    func(cmd_list)
                else:
                    print("Invalid cmd.")

    def __md5_required(self, cmd_list):
        '''检测命令是否需要进行MD5验证'''
        if '--md5' in cmd_list:
            return True

    def show_progress(self, total):
        received_size = 0
        current_percent = 0
        while received_size < total:
            if int((received_size / total) * 100) > current_percent:
                print("#", end="", flush=True)
                current_percent = int((received_size / total) * 100)
            new_size = yield
            received_size += new_size

    def _get(self, cmd_list):
        print("get--", cmd_list)
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        data_header = {
            'action': 'get',
            'filename': cmd_list[1]
        }
        if self.__md5_required(cmd_list):
            data_header['md5'] = True

        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        print(response)
        if response["status_code"] == 257:  # ready to receive
            self.sock.send(b'1')  # send confirmation to server
            base_filename = cmd_list[1].split('/')[-1]
            received_size = 0
            file_obj = open(base_filename, "wb")
            if self.__md5_required(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(response['file_size'])  # generator
                progress.__next__()
                while received_size < response['file_size']:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        print("100%")
                    file_obj.write(data)
                    md5_obj.update(data)
                else:
                    print("----->file rece done----")
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    md5_from_server = self.get_response()
                    if md5_from_server['status_code'] == 258:
                        if md5_from_server['md5'] == md5_val:
                            print("%s 文件一致性校验成功!" % base_filename)
                            # print(md5_val,md5_from_server)

            else:
                progress = self.show_progress(response['file_size'])  # generator
                progress.__next__()

                while received_size < response['file_size']:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    file_obj.write(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        print("100%")

                else:
                    print("----->file rece done----")
                    file_obj.close()

if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()  # 交互