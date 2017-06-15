#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用户家目录
USER_HOME = '%s/home' % BASE_DIR

# 帐号文件路径
ACCOUNT_FILE = '%s/conf' % BASE_DIR

# 服务器IP 端口号
HOST = "0.0.0.0"
PORT = 10021

