#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import threading
import time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run', n)
    semaphore.release()

if __name__ == '__main__':
    # 信号量设置
    semaphore = threading.BoundedSemaphore(5)
    for i in range(10):
        t = threading.Thread(target=run, args=('t%s' % i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print("All threads done")