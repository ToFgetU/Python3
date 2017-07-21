#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
import shutil
import os.path
import time

file_path = {
    '/app/lis/bank/xmlReturnFromBankFile': ['3m', 1], # 3m: 保留时间， 1: 需要备份， 0: 不需要备份
    '/app/lis/bank/xmlSendToBankFile': ['3m', 1],
    '/app/lis/dataupload': ['1y', 0],
    '/app/lis/vtsfile': ['1m', 0],
    '/app/lis/ehome/malldata/Endorsement': ['1y', 1],
    '/app/lis/ehome/malldata/notice': ['1y', 1],
    '/app/lis/xmlprintdata': ['1y', 0], # 同时对子目录进行处理
    '/app/lis/xmlprintdata/ehome': ['3m', 1],
    '/app/lis/xmlprintdata/icbcauto': ['3m', 1],
    '/app/lis/xmlprintdata/wgbq': ['1y', 1],
    '/app/lis/xmlprintdata/zjcheck': ['3m', 1],
    '/app/lis/xmlprintdata/': ['3m', 1], # /app/lis/xmlprintdata/(日期)日期文件夹备份
    '/app/lis/xmlprintdata/receive': ['3m', 1]
}

def do_bak(path, RetentionTime, backup):
    if os.path.exists(path):
        files = os.listdir(path)
        print(type(files))
        if path == "/app/lis/xmlprintdata/":
            for f in files:
                file = os.path.join(path, f)
                if os.path.isdir(file):
                    modify_time = os.path.getmtime(file)
                    print('time', modify_time)
                else:
                    pass