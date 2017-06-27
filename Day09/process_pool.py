#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

from multiprocessing import Process, Pool
import os
import time

def run(n):
    time.sleep(1)
    print('process %s:' % n, os.getpid())
    return n+100

def bar(arg):
    print('--> exec done %s' % arg, os.getpid())

if __name__ == '__main__':
    pool = Pool(processes=5) # 允许进程池同时放入五个进程
    print(os.getpid()) #主进程
    for i in range(10):
        # pool.apply(func=run, args=(i,)) #串行
        # pool.apply_async(func=run, args=(i,)) #并行
        pool.apply_async(func=run, args=(i,), callback=bar) #callback 回调
    print('end')
    # 必须先关闭进程池
    pool.close()
    pool.join()
