#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import threading
import time

def run(n):
    for i in range(10):
        print('%s: %s' % (n, i))
        time.sleep(0.5)

t1 = threading.Thread(target=run, args=('t1',))
t2 = threading.Thread(target=run, args=('t2',))

# t1 变为守护线程
t1.setDaemon(True)
t1.start()
t2.start()