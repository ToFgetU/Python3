#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import time

def consumer(name):
    print("$s 准备吃包子啦", name)
    while True:
        baozi = yield

        print("客户 %s 准备吃第[%s]个包子"% (name, baozi))

def producer(max):
    c1 = consumer('A')
    c2 = consumer('B')

    c1.__next__()
    c2.__next__()

    print("准备做包子啦")
    for i in range(max):
        time.sleep(1)
        print("第%s个包子"% i)
        c1.send(i)
        c2.send(i)

producer(10)