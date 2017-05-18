#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import login

def run():
    """
    This function will be called right a way when the program started, here handles the user interaction stuff
    """
    logined_sign = {}
    def change_to(t):
        """该函数的主要功能是选择目的地"""
        while True:
            username = input("请输入用户名: ").strip()
            password = input("请输入密码:").strip()
            if username in logined_sign:
                logined_sign[username] += 1
            else:
                logined_sign[username] = 1
            if logined_sign[username] >= 3:
                exit("The account %s is locked."% username)
                break
            else:
                name = login.user_login(username, password, login.mode(t))
                login.manager(name)
                break


    print("""
    你打算去哪？
    -->1. 去银行
    -->2. 去超市
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



run()