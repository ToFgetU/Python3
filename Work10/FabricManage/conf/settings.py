#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

# import os
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# #主机列表文件
# HOSTS_FILE = '%s/conf/hosts.json' % BASE_DIR
#
# #用户文件
# USER_PASSWORD_FILE = '%s/conf/user_passwd.cfg' % BASE_DIR

hosts_dict = {
    'test': [('192.168.128.133', 22), ('192.168.128.133', 22)],
    'test1': [('10.20.2.88', 22)]
}

user_dict = {
    '192.168.128.133': {
        'username': 'root',
        'password': '123456'
    },
    '10.20.2.99': {
        'username': 'root',
        'password': '123456'
    }
}