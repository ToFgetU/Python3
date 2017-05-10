#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import time
def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("the func run time %s"% (stop_time-start_time))
    return deco

@timer #test1 = timer(test1)
def test1():
    time.sleep(1)
    print("in the test1")

@timer
def test2(name):
    time.sleep(1)
    print("name: ", name)

#test1 = timer(test1) #获取的deco的内存地址，所以执行test1()，实际上就是执行deco()
test1()  #deco()

# timer 分解步骤如下
test2 = timer(test2) # 把deco的内存地址给了test2,所以执行test2()，实际上就是执行deco()
print("test2: ", test2)
test2("lilei")  #deco("lilie")