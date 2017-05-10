#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import time

username = "alex"
password = "abc123"
def auth(mode):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            if mode == "local":
                start_time = time.time()
                rec =func(*args, **kwargs)
                stop_time = time.time()
                print("the func run time is %s"% (stop_time-start_time))
                return rec
            elif mode == "ldap":
                print("in the ldap")
                start_time = time.time()
                rec = func(*args, **kwargs)
                stop_time = time.time()
                print("the func run time is %s" % (stop_time - start_time))
                return rec
        return wrapper
    return out_wrapper


def index():
    print("Welcome in the index page")

@auth(mode="local") #  home=wrapper()
def home(name):
    print("in the home", name)
    return "from home"

#@auth(mode="ldap")
def bbs():
    print("in the bbs")

index()
home("alex")

# @auth(mode="ldap") 分解步骤如下
#out_wrapper = auth(mode="ldap")  # 把 out_wrapper 内存地址给了 out_wrapper
# print("aa:", out_wrapper)
#bbs = out_wrapper(bbs)  # 把 wapper 的内存地址给了bbs,所以执行bbs()，实际上就是执行wapper(),
bbs = auth(mode="ldap")(bbs)  #两步整合的结果： bbs = auth(mode="ldap")(bbs)
print("bbs:", bbs)
bbs()

