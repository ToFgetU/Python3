#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Panfei Liu

"""
购物车程序：
1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录
"""
product = []
with open("data/product.txt", encoding='utf-8') as product_list:
    for pl in product_list.readlines():
        product.append(pl.rstrip())
print(product)

username = input("username: ")
password = input("password: ")

user_dict = {}
salary_dict = {}
user_buy = {}
while True:
    with open("data/user.txt", "r") as user_sign:
        for u in user_sign.readlines():
            user_passwd = u.split(":")
            user_dict[user_passwd[0]] = user_passwd[1].rstrip()

    with open("data/user.txt", "r") as salary_sign:
        for u in user_sign.readlines():
            user_passwd = u.split(":")
            user_dict[user_passwd[0]] = user_passwd[1].rstrip()

    #判断用户是否已经存在，如果不存在添加到 user.txt 文件中
    if username not in user_dict:
        with open("data/user.txt", "a") as user_sign:
            user_sign.writelines(username + ":" + password)
        with open("data/salary.txt", "a") as salary_sign:
            salary = input("-->Input your salary: ")
            salary.writelines(username + ":" + salary)
    else:
        break

#账号登入
if username in user_dict and password == user_dict[username]:
    print("-----> Welcome :", username + '\n')

    while True:
        print("----- product list -----")
        for index, item in enumerate(product):
            print(index, item)

        user_choice = input("Please choose the items what you want >>> ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if item[user_choice][1] < salary_sign[username]:
                salary_sign[username] -= item[user_choice][1]

                print("The item %s is already add in your cart, your \033[32;1m%s[0m: "% (item[user_choice][0], salary))
        break