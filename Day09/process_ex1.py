#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import multiprocessing
import threading
import time

def t_run():
    print(threading.get_ident())

def run(n):
    print('hello %s' % n)
    t = threading.Thread(target=t_run,)
    t.start()
    time.sleep(1)

if __name__ == '__main__':
    p = multiprocessing.Process(target=run, args=('pop',))
    p.start()