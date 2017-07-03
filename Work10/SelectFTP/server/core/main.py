#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import socket
from core.ftpserver import SelectFtpServer

def authentication():
    s = SelectFtpServer()
    s.start()



