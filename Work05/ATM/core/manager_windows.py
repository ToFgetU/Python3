#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import json
from core import login
from core.login import login_required

def add_account(t):
    """添加账户"""
    account = login.user_data(t)
    while True:
        username = input("输入账户名:").strip()
        while username in account:
            print("账户已存在")
            username = input("输入账户名:").strip()
        password = input("输入账户密码:").strip()
        again_p = input("再次输入账户密码:").strip()
        if password == again_p:
            while True:
                quo = input("请输入信用额度(默认请回车):")
                if quo.replace('.', '', 1).isdigit():
                    quo = eval(quo)
                    quota = user_quota(quota=quo)
                    break
                elif quo.strip():
                    print("输入格式有误")
                else:
                    quota = user_quota()
                    break
            account[username] = {
                'password': password,
                'quota': quota,
                'balance': quota,
                'acc_frozen': 0,
                'is_admin': 0
            }

            with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
                f.write(json.dumps(account, indent=4, separators=(',', ':')))
                print("账户 %s 添加成功"% username)
                break
            input("\n回车返回主菜单")
        else:
            print("两次密码不同，请重新输入")


def del_account(t):
    """删除账户"""
    account = login.user_data(t)
    username = input("输入要删除的账户名:").strip()
    if username not in account:
        print("要删除的用户 %s 不存在" % username)
    elif account[username]['is_admin']:
        print("%s 是管理员用户，不允许删除" % username)
    else:
        del account[username]
        with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(account, indent=4, separators=(',', ':')))
            print("用户 %s 已删除"% username)
            input("\n回车返回主菜单")


def user_quota(*args, quota=15000):
    """调整账户信用额度"""
    if args:
        account = login.user_data(args[0])
        username = input("输入要调整的账户名:").strip()
        if username not in account:
            print("要调整的账户名 %s 不存在"% username)
        elif account[username]['is_admin']:
            print("%s 是管理员用户，不允许操作" % username)
        else:
            while True:
                quota = input("输入调整后信用额度: ")
                if quota.replace('.', '', 1).isdigit():
                    quota = eval(quota)
                    break
                else:
                    print("输入的金额有误，请重新输入")

            account[username]['balance'] += quota - account[username]['quota']
            account[username]['quota'] = quota
            with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
                f.write(json.dumps(account, indent=4, separators=(',', ':')))
                print("账户 %s 信用额度调整为: %d" % (username, quota))
                input("\n回车返回主菜单")
                # return
    else:
        return quota

def frozen_account(t):
    """冻结账户"""
    account = login.user_data(t)
    username = input("输入要冻结的账户名:").strip()
    if username not in account:
        print("要冻结的账户 %s 不存在" % username)
    elif account[username]['is_admin']:
        print("%s 是管理员用户，不允许操作" % username)
    else:
        account[username]['acc_frozen'] = 1
        with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(account, indent=4, separators=(',', ':')))
            print("用户 %s 已冻结" % username)
        input("\n回车返回主菜单")

def thaw_account(t):
    """解冻账户"""
    account = login.user_data(t)
    username = input("输入要解冻的账户名:").strip()
    if username not in account:
        print("要解冻的账户 %s 不存在" % username)
    elif account[username]['is_admin']:
        print("%s 是管理员用户，不允许操作" % username)
    else:
        account[username]['acc_frozen'] = 0
        with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(account, indent=4, separators=(',', ':')))
            print("用户 %s 已解冻" % username)
        input("\n回车返回主菜单")


@login_required
def manager(*args):
    """管理员入口"""
    print("我是管理员窗口", args[0])
    menu = u'''
        -------  Bank Manager -------
        \033[32;1m\t菜单信息
        \t1.  添加账户
        \t2.  删除账户
        \t3.  用户额度
        \t4.  冻结账户
        \t5.  解冻账户
        \t6.  退出
        \033[0m'''
    menu_dic = {
        '1': add_account,
        '2': del_account,
        '3': user_quota,
        '4': frozen_account,
        '5': thaw_account,
        '6': 'logout',
    }
    while True:
        print(menu)
        num = input("操作选择: ").strip()
        if num == '1':
            menu_dic[num](args[1])
        elif num == '2':
            menu_dic[num](args[1])
        elif num == '3':
            menu_dic[num](args[1])
        elif num == '4':
            menu_dic[num](args[1])
        elif num == '5':
            menu_dic[num](args[1])
        elif num == '6':
            exit("退出程序")
        else:
            print("输入有误，请重新输入")




