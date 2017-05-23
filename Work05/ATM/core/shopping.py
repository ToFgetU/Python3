#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
import json
from core import general_windows
from core.login import login_required


def shopping_data():
    """读取账单数据信息"""
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, "../data/shopping.json"), "r", encoding='utf-8') as f:
        goods = json.loads(f.read())
        return goods

def shopping_info():
    """读取账单数据信息"""
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, "../data/shopping_info.json"), "r", encoding='utf-8') as f:
        info = json.loads(f.read())
        return info

def shopping_tmp():
    """读取账单数据信息"""
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, "../data/shopping_tmp.json"), "r", encoding='utf-8') as f:
        tmp = json.loads(f.read())
        return tmp

def goods_list(*args):
    "商品信息列表"
    goods = shopping_data()
    # print(goods)
    old_cart = shopping_info()
    # print(old_cart)
    # print(type(old_cart))
    new_cart = {}

    while True:
        for key, values in goods.items():
            print(key, values)
        change_goods = input("请输入要购买的商品(退出: exit):").strip()
        if change_goods in goods:
            # print(type(old_cart))
            if args[0] in old_cart:
                if change_goods in old_cart[args[0]]:
                    old_cart[args[0]][change_goods]['num'] += 1
                else:
                    old_cart[args[0]][change_goods] = {'price': goods[change_goods], 'num': 1}
                if change_goods in new_cart:
                    new_cart[change_goods]['num'] += 1
                else:
                    new_cart[change_goods] = {'price': goods[change_goods], 'num': 1}
            else:
                old_cart[args[0]] = {change_goods: {'price': goods[change_goods], 'num': 1}}
                new_cart[change_goods] = {'price': goods[change_goods], 'num': 1}
        elif change_goods.lower() == 'exit':
            break
        else:
            print("输入的商品不存在")
            input("\n回车返回商品列表")
        # print(old_cart)
        # print(new_cart)
    with open("../data/shopping_info.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(old_cart, indent=4, separators=(',', ':')))
    with open("../data/shopping_tmp.json", 'w', encoding='utf-8') as tmp_f:
        tmp_f.write(json.dumps(new_cart, indent=4, separators=(',', ':')))
    input("\n回车返回主菜单")


def cart_list(*args):
    """只现实了购物车显示功能，还需要清空购物车和删除某个商品"""
    new_cart = shopping_tmp()
    old_cart = shopping_info()

    print("购物车中的商品:")
    for key, values in new_cart.items():
        print("\t", key, values)

def checkout(*args):
    """结账操作"""
    new_cart = shopping_tmp()
    old_cart = shopping_info()

    do_it = input("是否前往结账（Y/N）: ")
    if do_it.lower() == 'y':
        username = input("请登入支付账户: ").strip()
        password = input("请输入支付密码: ").strip()

        sum = 0
        for i in new_cart:
            print(new_cart[i]['price'])
            sum += new_cart[i]['price']
        buy_sucess = general_windows.topay(username, password, sum)
        if buy_sucess:
            new_cart = {}
            with open("../data/shopping_tmp.json", 'w', encoding='utf-8') as tmp_f:
                tmp_f.write(json.dumps(new_cart, indent=4, separators=(',', ':')))
        else:
            print("购物失败，请确认账户信息是否正确或有足够的余额。")

@login_required
def shopping_cart(*args):
    """商店入口"""
    menu = u'''
            -------  Shopping Windows -------
            \033[32;1m\t菜单信息
            \t1.  商品列表
            \t2.  查看购物车
            \t3.  结账
            \t4.  退出
            \033[0m'''
    menu_dic = {
        '1': goods_list,
        '2': cart_list,
        '3': checkout,
        '4': 'logout',
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
            exit("退出程序")
            logger_conf.logger.debug("%s 退出程序" % args[0])
        else:
            print("输入有误，请重新输入")
