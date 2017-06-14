#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import json
import configparser
import socketserver

from conf import settings

STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",
}

class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.data)
            print(self.client_address[0])

            if not self.data:
                print("client closed")
                break

            data = json.loads(self.data.encode())
            if data.get("action") is not None:
                print("----> ", hasattr(self, "_auth"))
                if hasattr(self, "_%s" % data.get("action")):
                    func = getattr(self, "_%s" % data.get("action"))
                    func()
                else:
                    print("invalid cmd")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)

    def send_response(self, status_code, data = None):
        '''向客户端返回数据'''
        response = {
            'status_code': status_code,
            'status_msg': STATUS_CODE[status_code]
        }

        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        data = args[0]
        if data.get("username") is None or data.get("password") is None:
            self.send_response(252)
        user = self.authenticate(data.get("username"), data.get("password"))
        if user is None:
            self.send_response(253)
        else:
            print("passed authentication", user)
            self.user = user
            self.send_response(254)

    def authenticate(self, username, password):
        '''验证用户合法性'''
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print("auth pass...", username)
                config[username]["Username"] = username
                return config[username]

    def _put(self, *args, **kwargs):
        "client send file to server"
        pass

    def _get(self, *args, **kwargs):
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)
        user_home_dir = "%s/%s" % (settings.USER_HOME, self.user["Username"])
        file_abs_path = "%s/%s" % (user_home_dir, data.get('filename'))
        print("file abs path", file_abs_path)

        if os.path.isfile(file_abs_path):
            file_obj = open(file_abs_path, "rb")
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257, data={'file_size': file_size})
            self.request.recv(1)  # 等待客户端确认

            if data.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.send_response(258, {'md5': md5_val})
                    print("send file done....")
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print("send file done....")
        else:
            self.send_response(256)

    def _ls(self, *args, **kwargs):
        pass

    def _cd(self, *args, **kwargs):
        pass
