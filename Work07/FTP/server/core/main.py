#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socketserver
import optparse
from conf import settings

class ArvgHandler(object):
    '''FTP服务端入口'''
    def __init__(self):
        self.parser = optparse.OptionParser()
        options, args = self.parser.parse_args()

        self.verify_args(options, args)

    def verify_args(self, options, args):
        '''校验 并调用相应功能'''
        if hasattr(self, args[0]):
            func = getattr(self, args[0])
            func()
        else:
            self.parser.print_help()

    def start(self):
        print("-----going to start server-----")
        server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), FTPHandler)
        server.serve_forever()

