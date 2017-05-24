#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu
import json
import os

def user_data(t):
    """读取数据信息"""
    base_dir = os.path.dirname(__file__)
    if t == 'shopping':
        with open(os.path.join(base_dir, "../data/shopping_user.json"), "r", encoding='utf-8') as f:
            account = json.loads(f.read())
            return account
    else:
        with open(os.path.join(base_dir, "../data/atm_user.json"), "r", encoding='utf-8') as f:
            account = json.loads(f.read())
            return account

def billing_data():
    """读取账单数据信息"""
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, "../data/billing_info.json"), "r", encoding='utf-8') as f:
        info = json.loads(f.read())
        return info

# def login_auth(func):
#     """用户登入选择"""
#     def wrapper(*args, **kwargs):
#         print(args)
#         if args[1] == 'admin':
#             return func(*args, **kwargs)
#         elif args[1] =='atm':
#             return func(*args, **kwargs)
#         else:
#             return func(*args, **kwargs)
#     return wrapper

LOGIN_SIGN = {}
def login_required(func):
    """验证用户是否登录"""
    def wrapper(*args, **kwargs):
        account = user_data(args[1])
        # print(args)
        if args[0] in LOGIN_SIGN:
            if args[1] != 'admin':
                if args[1] == 'atm':
                    if account[args[0]]['is_admin']:
                        exit("User is not authenticated.")
                    else:
                        return func(*args, **kwargs)
                else:
                    return func(*args, **kwargs)
            else:
                if account[args[0]]['is_admin']:
                    return func(*args, **kwargs)
                else:
                    exit("User is not authenticated.")
        else:
            exit("User is not authenticated.")
    return wrapper

# @login_required
# @login_auth(mode=mode)
def user_login(name, password, mode):
    account = user_data(mode)
    if name in account:
        if password == account[name]['password']:
            # print("%s 登入成功"% name, mode)
            LOGIN_SIGN[name] = 1
            # print(LOGIN_SIGN)
            return name
        else:
            print("User or password is not correct")
    else:
        print("User or password is not correct")




# t = 'admin'
# mode(t)
# user_login()


