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
        # print(args)
        if LOGIN_SIGN[args[0]]:
            return func(*args, **kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper

# @login_required
# @login_auth(mode=mode)
def user_login(name, password, mode):
    account = user_data(mode)
    if name in account:
        if password == account[name]['password']:
            print("%s 登入成功"% name, password, mode)
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


