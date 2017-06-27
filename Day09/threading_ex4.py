#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import threading
import time

event = threading.Event()
def lighter():
    count = 0
    event.set()
    while True:
        if count >=5 and count < 10:
            event.clear()
            print('红灯')
        elif count == 10:
            count = 0
            event.set()
            continue
        else:
            print('绿灯')
        count += 1
        time.sleep(1)

def car(n):
    while True:
        if event.is_set():
            print('%s is running ...' % n)
        else:
            print('%s is stoped ...' % n)
        time.sleep(1)

light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car, args=('car1',))
car1.start()