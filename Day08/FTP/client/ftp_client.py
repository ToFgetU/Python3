#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
import optparse

class FTPClient(object):
    def __init__(self):
        parse = optparse.OptionParser()
        parse.add_option("-s", "--server", dest="server", help="ftp server ip addr")
        parse.add_option("-P", "--Port", dest="port", help="ftp server port")
        parse.add_option("-u", "--username", dest="username", help="ftp server user")
        parse.add_option("-p", "--password", dest="password", help="ftp server password")
        (self.opstions, self.args) = parse.parse_args()


