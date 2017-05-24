#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import json

from core import login
from core import manager_windows as m
from core import general_windows as g
from core import shopping as s

def run():
    """
    This function will be called right a way when the program started, here handles the user interaction stuff
    """
    logined_sign = {}
    def change_to(t):
        """该函数的主要功能是选择目的地"""
        account = login.user_data(t)
        while True:
            username = input("请输入用户名: ").strip()
            password = input("请输入密码:").strip()
            if username in account and t != 'shopping':
                if account[username]['is_admin']:
                    if username in logined_sign:
                        logined_sign[username] += 1
                    else:
                        logined_sign[username] = 1
                    if logined_sign[username] >= 3:
                        exit("The account %s is locked."% username)
                    else:
                        name = login.user_login(username, password, t)
                        if t == 'admin':
                            m.manager(name, t)
                        elif t == 'atm':
                            g.gen_user(name, t)
                        else:
                            s.shopping_cart(name, t)
                if account[username]['acc_frozen']:
                    print("账户已冻结")
                else:
                    if username in logined_sign:
                        logined_sign[username] += 1
                    else:
                        logined_sign[username] = 1
                    if logined_sign[username] >= 3:
                        exit("The account %s is locked."% username)
                    else:
                        name = login.user_login(username, password, t)
                        if t == 'admin':
                            m.manager(name, t)
                        elif t == 'atm':
                            g.gen_user(name, t)
                        else:
                            s.shopping_cart(name, t)
            elif username not in account and t == 'shopping':
                what_do = input("该用户不存在，是否注册(Y/N)").strip()
                if what_do.lower() == 'y':
                    password = input("请设置密码:").strip()
                    account[username] = {'password': password}
                    with open("../data/shopping_user.json", 'w', encoding='utf-8') as f:
                        f.write(json.dumps(account, indent=4, separators=(',', ':')))
                    break
            else:
                if username in logined_sign:
                    logined_sign[username] += 1
                else:
                    logined_sign[username] = 1
                if logined_sign[username] >= 3:
                    exit("The account %s is locked." % username)
                else:
                    name = login.user_login(username, password, t)
                    if t == 'admin':
                        m.manager(name, t)
                    elif t == 'atm':
                        g.gen_user(name, t)
                    else:
                        s.shopping_cart(name, t)


    print("""
    你打算去哪？
    -->1. 去银行
    -->2. 去购物
    """)

    change = input("您的选择是: ")

    if change.strip() == '1':
        is_admin = input("您是管理员吗(Y/N) : ")
        if is_admin.lower() == 'y':
            t = 'admin'
            change_to(t)
        else:
            t = 'atm'
            change_to(t)
    elif change.strip() == '2':
        t = 'shopping'
        change_to(t)
    else:
        print("您选择了其他地方，再见。。。")

