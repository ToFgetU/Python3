#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import json
import socketserver

class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])