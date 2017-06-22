#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socketserver
import json
import optparse
from conf import settings
from core.ftp_server import FTPHandler

class ArvgHandler(object):
    def __init__(self):
        parse = optparse.OptionParser()
        (self.options, self.args) = parse.parse_args()
        # print(self.options, self.args)

        self.verify_args(self.options, self.args)

    def verify_args(self, options, args):
        try:
            a = args[0].strip()
            if hasattr(self, a):
                func = getattr(self, a)
                func()
        except Exception as e:
            print("没有输入启动参数 start")


    def start(self):
        '''启动FTP服务'''
        print("----- going to start server -----")
        server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), FTPHandler)
        server.serve_forever()



