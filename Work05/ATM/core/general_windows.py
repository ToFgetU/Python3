#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import json
from core import login
from core.login import login_required

def account_info(*args):
    """账户信息查询"""
    # print(args)
    account = login.user_data(args[1])
    print("账户信息:")
    print("\t您的账户: ", args[0])
    print("\t信用额度: ", account[args[0]]['quota'])
    print("\t可用额度: ", account[args[0]]['balance'])
    input("\n回车返回主菜单")

def withdrawal(*args):
    """用户提现，只能提现信用额度的一半，并需要扣除%5手续费"""
    account = login.user_data(args[1])
    quota = account[args[0]]['quota']
    balance = account[args[0]]['balance']
    while True:
        wd = input("请输入取现金额: ").strip()
        if wd.isdigit():
            wd = int(wd)
            break
        else:
            print("输入有误")
    if wd > quota/2:
        print("您的可提现金额不能超过 %d" % quota/2)
    elif wd * 1.05 > balance:
        print("您的可用金额还有 %d，不够提现" %balance)
    else:
        account[args[0]]['balance'] = balance - wd * 1.05
        with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(account, indent=4, separators=(',', ':')))
            print("账户 %s 本次提现了 %d, 扣除手续费 %d, 可用余额还有 %d"
                  % (args[0], wd, wd*0.05, account[args[0]]['balance']))
        input("\n回车返回主菜单")


def transfer(*args, quota = 15000):
    """调整账户信用额度"""


def repay(t):
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

def pay_check(t):
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


@login_required
def gen_user(*args):
    """普通账户入口"""
    print("我是普通用户窗口", args[0])
    menu = u'''
        -------  Bank Windows -------
        \033[32;1m\t菜单信息
        \t1.  账户信息
        \t2.  提现
        \t3.  转账
        \t4.  还款
        \t5.  账单查询
        \t6.  退出
        \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': withdrawal,
        '3': transfer,
        '4': repay,
        '5': pay_check,
        '6': 'logout',
    }
    while True:
        print(menu)
        num = input("操作选择: ").strip()
        if num == '1':
            menu_dic[num](args[0], args[1])
        elif num == '2':
            menu_dic[num](args[0], args[1])
        elif num == '3':
            menu_dic[num](args[0], args[1])
        elif num == '4':
            menu_dic[num](args[0], args[1])
        elif num == '5':
            menu_dic[num](args[0], args[1])
        else:
            break




