#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
import shutil
import os.path
import time
import threading

file_path = {
    'bank/xmlReturnFromBankFile': ['3m', 1], # 3m: 保留时间， 1: 需要备份， 0: 不需要备份
    'bank/xmlSendToBankFile': ['3m', 1],
    'dataupload': ['1y', 0],
    'vtsfile': ['1m', 0],
    'ehome/malldata/Endorsement': ['1y', 1],
    'ehome/malldata/notice': ['1y', 1],
    'xmlprintdata': ['1y', 0], # 同时对子目录进行处理
    'xmlprintdata/ehome': ['3m', 1],
    'xmlprintdata/icbcauto': ['3m', 1],
    'xmlprintdata/wgbq': ['1y', 1],
    'xmlprintdata/zjcheck': ['3m', 1],
    'xmlprintdata/': ['3m', 1], # /app/lis/xmlprintdata/(日期)日期文件夹备份
    'xmlprintdata/receive': ['3m', 1]
}

def do(file, path, RetentionTime, backup):
    now_time = time.time()
    dest = '/home/data_mount/ilis/file_bak/%s' % path
    modify_time = os.path.getmtime(file)
    if os.path.exists(dest):
        pass
    else:
        os.makedirs(dest)
    if RetentionTime == '3m' and (now_time - modify_time) / (60 * 60 * 24) > 90:
        if backup:
            result = os.popen('mv -f %s %s' % (file, dest))
            print(result)
        else:
            result = os.popen(('rm -rf %s %s' % (file, dest)))
            print(result)
    elif RetentionTime == '1y' and (now_time - modify_time) / (60 * 60 * 24) > 365:
        if backup:
            result = os.popen('mv -f %s %s' % (file, dest))
            print(result)
        else:
            result = os.popen(('rm -rf %s %s' % (file, dest)))
            print(result)
    elif RetentionTime == '1m' and (now_time - modify_time) / (60 * 60 * 24) > 30:
        if backup:
            result = os.popen('mv -f %s %s' % (file, dest))
            print(result)
        else:
            result = os.popen(('rm -rf %s %s' % (file, dest)))
            print(result)
    else:
        pass


def do_bak(path, RetentionTime, backup):
    print(path, RetentionTime, backup)
    p = '/app/lis/%s' % path
    if os.path.exists(p):
        files = os.listdir(p)
        print(type(files))
        if p == "/app/lis/xmlprintdata/":
            for f in files:
                file = os.path.join(p, f)
                if os.path.isdir(file):
                    do(file, path, RetentionTime, backup)
                else:
                    pass
        else:
            if p == '/app/lis/xmlprintdata':
                for f in files:
                    file = os.path.join(p, f)
                    if os.path.isfile(file):
                        do(file, path, RetentionTime, backup)
            else:
                for f in files:
                    file = os.path.join(p, f)
                    do(file, path, RetentionTime, backup)

def start_run():
    for p, v in file_path.items():
        print(p, v)
        t = threading.Thread(target=do_bak, args=(p, v[0], v[1]))
        t.start()


if __name__ == '__main__':
    start_run()