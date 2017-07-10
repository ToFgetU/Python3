#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用户家目录
USER_HOME = '%s/home' % BASE_DIR
print(USER_HOME)

user_dict = {
    'test': 'test',
    'alex': '123',
    'hello': '123'
}

host_port = ('0.0.0.0', 10021)