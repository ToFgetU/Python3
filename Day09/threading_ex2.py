#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import threading
import time

num = 0
lock = threading.Lock()
def run(n):
    global num
    # 互斥锁
    lock.acquire()
    num += 1
    # 释放锁
    lock.release()


for j in range(500):
    t = threading.Thread(target=run, args=('t-%s' % j,))
    t.start()
    t1 = threading.Thread(target=run, args=('t1-%s' % j,))
    t1.start()

print(num)

