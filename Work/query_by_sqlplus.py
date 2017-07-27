#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
import os.path
import datetime
import re

env = input('请选择环境(1-准生产;2-生产):').strip()  #1-准生产;2-生产
rootdir = input('请输入脚本路径：').strip()

if env == '1':
	user_code = 'liscode'
	user_base = 'lisbase'
	user_data = 'lisdata'
	pwd_code = 'liscode432u1'
	pwd_base = 'lisbase643u1'
	pwd_data = 'lisdata531u1'
	db_name = 'stgdb'
elif env == '2':
	user_code = 'songj[liscode]'
	user_base = 'songj[lisbase]'
	user_data = 'songj[lisdata]'
	pwd_code = 'zxcvbnm,.123'
	pwd_base = 'zxcvbnm,.123'
	pwd_data = 'zxcvbnm,.123'
	db_name = 'lis'

now = datetime.datetime.now()

dir_list = ['struts_base', 'struts_data', 'View', 'Sequence', 'Trigger', 'Function', 'Procedure', 'Package',
            'Package_Body', 'menu', 'modify_base', 'modify_data']



def QueryBySqlplus():
    with open('file_obj.txt', r) as f:
        for line in f:
            print(line)


def start():
    count = 0
    for dir in dir_list:
        count += 1
        path_dir = os.path.join(rootdir, dir)
        for path, dirnames, filenames in os.walk(path_dir):
            print(path, dirnames, filenames)
            for filename in filenames:
                path_file = os.path.join(path_dir, filename)
                with open(path_file, 'r') as pf:
                    if '/*' in pf and '*/' in pf.read():
                        print('%s 存在 /**/' % filename)
                with open('file_obj.txt', 'a+') as f:
                    f.write('@ '+path_file+'\n')
        if count == 2 or count == 12:
            print('lisbase, lisdata 授权')
        elif count == 10:
            print('liscode 授权')

