#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import optparse
import socketserver
from conf import settings
from core.ftp_server import FTPHandler

class ArvgHandler(object):
    def __init__(self):
        self.parse = optparse.OptionParser()
        # self.parse.add_option("-s", "--host", dest = "host", help = "server binding host address")
        # self.parse.add_option("-p", "--port", dest = "port", help = "server binding port")
        (options, args) = self.parse.parse_args() # 获取参数，返回元组
        print(options, args)
        self.verify_args(options, args)

    def verify_args(self, options, args):
        if hasattr(self, args[0]):
            func = getattr(self, args[0])
            func()
        else:
            self.parse.print_help()

    def start(self):
        print("----- going to start server -----")
        server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), FTPHandler())
        server.serve_forever() #启动监听