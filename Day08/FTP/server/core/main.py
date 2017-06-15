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
        self.start()
        parse = optparse.OptionParser()
        (self.options, self.args) = parse.parse_args()
        print(self.options, self.args)

    def start(self):
        '''启动FTP服务'''
        print("----- going to start server -----")
        server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), FTPHandler)
        server.serve_forever()



