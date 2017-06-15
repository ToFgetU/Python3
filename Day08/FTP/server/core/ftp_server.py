#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socketserver
import json

class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.data)
            print(self.client_address)

            if not self.data:
                print("client [%s] closed" % self.client_address)
                break
            data = json.loads(self.data.encode())
            if data.get('action'):
                if hasattr(self, data.get('action')):
                    func = getattr(self, data.get('action'))
                    func()


