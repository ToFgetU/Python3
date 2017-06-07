#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import uuid
import hashlib
import time

def create_uuid():
    '''生成UUID号'''
    return str(uuid.uuid1())

def create_md5():
    '''生成md5'''
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()

if __name__ == '__main__':
    x = create_uuid()
    print(x)

    x = create_md5()
    print(x)