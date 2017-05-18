#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu
import json
def user_data(t):
    """读取数据信息"""
    if t == 'shopping':
        with open("../data/shopping_user.json", "r", encoding='utf-8') as f:
            account = json.loads(f.read())
            return account
    else:
        with open("../data/atm_user.json", "r", encoding='utf-8') as f:
            account = json.loads(f.read())
            return account

def mode(t):
    if t == 'admin':
        return 'admin'
    elif t == 'atm':
        return 'atm'
    else:
        return 'shopping'

def login_auth(mode):
    """用户登入选择"""
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


def login_required(func):
    """验证用户是否登录,如果用户密码错误超过三次提示错误信息并退出程序"""
    def wrapper(*args, **kwargs):
        if args[1] == '123':
            return func(*args, **kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper

@login_required
@login_auth(mode=mode)
def user_login(name, password, mode):
    account = user_data(mode)
    if name in account:
        if password == account[name]['password']:
            print("%s 登入成功"% name, password, mode)
    else:
        print("User or password is not correct")

# t = 'admin'
# mode(t)
# user_login()


