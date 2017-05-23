#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import json
import time
import datetime
from core import login
from core.login import login_required
from conf import logger_conf

def account_info(*args):
    """账户信息查询"""
    # print(args)
    account = login.user_data(args[1])
    print("账户信息:")
    print("\t您的账户: ", args[0])
    print("\t信用额度: ", account[args[0]]['quota'])
    print("\t可用额度: ", account[args[0]]['balance'])
    logger_conf.logger.debug("%s 查询了用户信息" % args[0])
    input("\n回车返回主菜单")

def withdrawal(*args):
    """用户提现，只能提现信用额度的一半，并需要扣除%5手续费"""
    account = login.user_data(args[1])
    billing = login.billing_data()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    quota = account[args[0]]['quota']
    balance = account[args[0]]['balance']
    while True:
        wd = input("请输入取现金额: ").strip()
        if wd.replace('.', '', 1).isdigit():
            wd = eval(wd)
            break
        else:
            print("输入有误")
    if wd > quota/2:
        print("您的可提现金额不能超过 %d" % (quota/2))
        logger_conf.logger.warn("您的可提现金额不能超过 %d" % (quota/2))
    elif wd * 1.05 > balance:
        print("您的可用金额还有 %d，不够提现" % balance)
        logger_conf.logger.warn("您的可用金额还有 %d，不够提现" % balance)
    else:
        account[args[0]]['balance'] = balance - wd * 1.05
        with open("../data/billing_info.json", 'w', encoding='utf-8') as fi:
            if args[0] in billing:
                billing[args[0]][now_time] = ('提现 %d, 手续费 %d' % (wd, wd*0.05))
                fi.write(json.dumps(billing, indent=4, separators=(',', ':')))
            else:
                billing[args[0]] = {now_time: ('提现 %d, 手续费 %d' % (wd, wd*0.05))}
                fi.write(json.dumps(billing, indent=4, separators=(',', ':')))
        with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
            f.write(json.dumps(account, indent=4, separators=(',', ':')))
            print("账户 %s 本次提现了 %d, 扣除手续费 %d, 可用余额还有 %d"
                  % (args[0], wd, wd*0.05, account[args[0]]['balance']))
            logger_conf.logger.debug("账户 %s 本次提现了 %d, 扣除手续费 %d, 可用余额还有 %d"
                  % (args[0], wd, wd*0.05, account[args[0]]['balance']))
        input("\n回车返回主菜单")


def transfer(*args):
    """转账"""
    account = login.user_data(args[1])
    balance = account[args[0]]['balance']
    billing = login.billing_data()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    while True:
        tran = input("请输入转账金额: ").strip()
        if tran.replace('.', '', 1).isdigit():
            tran = eval(tran)
            break
        else:
            print("输入有误")

    username = input("请输入转账用户: ").strip()
    if username == args[0]:
        print("您输入了自己的帐号，转账失败")
        logger_conf.logger.error("您输入了自己的帐号，转账失败")
    elif username in account:
        if tran > balance:
            print("余额不足，转账失败")
            logger_conf.logger.warn("余额不足，转账失败")
        else:
            account[args[0]]['balance'] = balance - tran
            account[username]['balance'] += tran
            with open("../data/billing_info.json", 'w', encoding='utf-8') as fi:
                if args[0] in billing:
                    billing[args[0]][now_time] = ('向 %s 转账 %d' % (username, tran))
                    fi.write(json.dumps(billing, indent=4, separators=(',', ':')))
                else:
                    billing[args[0]] = {now_time: ('向 %s 转账 %d' % (username, tran))}
                    fi.write(json.dumps(billing, indent=4, separators=(',', ':')))
            with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
                f.write(json.dumps(account, indent=4, separators=(',', ':')))
                print("账户 %s 本次向 帐号 %s 转账 %d"
                      % (args[0], username, tran))
                logger_conf.logger.debug("账户 %s 本次向 帐号 %s 转账 %d"
                      % (args[0], username, tran))
            input("\n回车返回主菜单")
    else:
        print("输入的账户不存在，请谨慎操作")
        logger_conf.logger.warn("输入的账户不存在，请谨慎操作")

def repay(*args):
    """还款"""
    account = login.user_data(args[1])
    billing = login.billing_data()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    quota = account[args[0]]['quota']
    balance = account[args[0]]['balance']
    need_repay = quota - balance
    while True:
        actual_repay = input("您的还款:")
        if actual_repay.replace('.', '', 1).isdigit():
            actual_repay = eval(actual_repay)
            with open("../data/billing_info.json", 'w', encoding='utf-8') as fi:
                if args[0] in billing:
                    billing[args[0]][now_time] = ('本月还款 %s' % actual_repay)
                    fi.write(json.dumps(billing, indent=4, separators=(',', ':')))
                else:
                    billing[args[0]] = {now_time: ('本月还款 %s' % actual_repay)}
                    fi.write(json.dumps(billing, indent=4, separators=(',', ':')))
            if actual_repay >= need_repay:
                # print("本月你已还款")
                logger_conf.logger.debug("本月 %s 已还款" % args[0])
                with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
                    f.write(json.dumps(account, indent=4, separators=(',', ':')))
                    print("账户 %s 应还款%d，本次还款 %d"
                          % (args[0], need_repay, actual_repay))
                    logger_conf.logger.debug("账户 %s 应还款%d，本次还款 %d"
                          % (args[0], need_repay, actual_repay))
                input("\n回车返回主菜单")
                break
            else:
                with open("../data/atm_user.json", 'w', encoding='utf-8') as f:
                    f.write(json.dumps(account, indent=4, separators=(',', ':')))
                    print("本月 %s 已还款 %d,还需要还款%s" % (args[0], actual_repay, need_repay - actual_repay))
                    logger_conf.logger.debug("本月 %s 已还款 %d,还需要还款%s" % (args[0], actual_repay, need_repay - actual_repay))
                input("\n回车返回主菜单")
                break


def pay_check(*args):
    """账单查询"""
    billing = login.billing_data()
    if args[0] in billing:
        logger_conf.logger.debug("--> 账单查询")
        year = input("请输入年份(默认不输为全部账单信息): ").strip()
        month = input("请输入月份(默认不输为全部账单信息): ").strip()
        if month.isdigit() and year.isdigit():
            for key, values in billing[args[0]].items():
                c_date = str(key).split('-')
                if int(month) == int(c_date[1]) and int(year) == int(c_date[0]):
                    print(key, values)
                    logger_conf.logger.debug(key + ' ' + values)
                else:
                    pass
        else:
            for key, values in billing[args[0]].items():
                print(key, values)
                logger_conf.logger.debug(key + ' ' + values)
            input("\n回车返回主菜单")
    else:
        print("该用户还没生成账单")
        logger_conf.logger.debug("该用户 %s 还没生成账单" % args[0])

def topay(username, password, pay):
    billing = login.billing_data()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    account = login.user_data('atm')
    balance = account[username]['balance']
    if username in account:
        if account[username]['acc_frozen']:
            print("账户已被冻结")
        elif account[username]['password'] == password:
            if balance >= pay:
                account[username]['balance'] = balance - pay
                with open("../data/billing_info.json", 'w', encoding='utf-8') as fi:
                    if username in billing:
                        billing[username][now_time] = ('购物支付 %d' % pay)
                        fi.write(json.dumps(billing, indent=4, separators=(',', ':')))
                        print("支付成功")
                    else:
                        billing[username] = {now_time: ('购物支付 %d' % pay)}
                        fi.write(json.dumps(billing, indent=4, separators=(',', ':')))
                        print("支付成功")
                return True
            else:
                print("账户余额不足")
                return False
        else:
            print("帐号或密码错误")
            return False

    else:
        print("输入的账户不存在")
        return False


@login_required
def gen_user(*args):
    """普通账户入口"""
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
        elif num == '6':
            exit("退出程序")
            logger_conf.logger.debug("%s 退出程序" % args[0])
        else:
            print("输入有误，请重新输入")




