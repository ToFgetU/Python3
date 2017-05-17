#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

def mode(t):
    if t == 'admin':
        return 'admin'
    elif t == 'atm':
        return atm
    else:
        return 'shopping'

def login_auth(mode):
    """用户登入选择装饰器"""
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            if mode == 'admin':
                return func(*args, **kwargs)
            elif mode == 'atm':
                return func(*args, **kwargs)
            else:
                return func(*args, **kwargs)
        return  wrapper
    return out_wrapper



@login_auth(mode=mode)
def user_login():
    print("登入成功")

t = 'admin'
mode(t)
user_login()