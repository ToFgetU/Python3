#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import ftp_server
if __name__ == '__main__':
    ftp_server.start()