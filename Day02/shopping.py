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
user_buy_dict = {}
cart = []
while True:
    #存储用户
    with open("data/user.txt", "r", encoding='utf-8') as user_sign:
        for u in user_sign.readlines():
            user_passwd = u.split(":")
            user_dict[user_passwd[0]] = user_passwd[1].rstrip()
            print(user_dict)
    #存储账户余额
    with open("data/salary.txt", "r", encoding='utf-8') as salary_sign:
        for s in salary_sign.readlines():
            user_passwd = s.split(":")
            salary_dict[user_passwd[0]] = int(user_passwd[1].rstrip())
    #存储购买记录到user_buy的字典中
    with open("data/user_buy_log.txt", "r", encoding='utf-8') as user_buy_sign:
        for ub in user_buy_sign.readlines():
            user_buy = ub.split(":")
            print(user_buy[0], user_buy[1])
            user_buy_dict[user_buy[0]] = user_buy[1].rstrip()
            print("--->", user_buy_dict)

    #判断用户是否已经存在，如果不存在添加到 user.txt 文件中
    if username not in user_dict:
        with open("data/user.txt", "a", encoding='utf-8') as user_sign:
            user_sign.writelines(username + ":" + password + "\n")
        with open("data/salary.txt", "a", encoding='utf-8') as salary_sign:
            salary = input("-->Input your salary: ")
            salary_sign.writelines(username + ":" + salary + "\n")
    else:
        break

#账号登入
if username in user_dict and password == user_dict[username]:
    print("-----> Welcome :", username + '\n')

    while True:
        print("----- product list -----")
        for index, item in enumerate(product):
            print("\t", index, item)
        #选择商品代码
        user_choice = input("Please choose the items what you want (quit:q/Q)>>> ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product) and user_choice >= 0:
                p_item = product[user_choice].split(",")
                p_name = p_item[0]
                p_salary = int(p_item[1].strip())
                if p_salary <= salary_dict[username]:
                    salary_dict[username] -= p_salary
                    cart.append(p_item)
                    print("The goods [\033[34;1m%s\033[0m] is already add in your cart, "
                          "your balance : \033[32;1m%d\033[0m "% (p_name, salary_dict[username]))
                else:
                    print("Your balance [\033[31;1m%s\033[0m] is not enough to "
                          "buy the goods [\033[34;1m%s\033[0m] . . ."% (salary_dict[username], p_name))
            else:
                print("No goods what you want...")
        elif user_choice in "qQ":
            #存储购买记录
            user_buy_dict[username] = cart
            with open("data/user_buy_log.txt", "a", encoding='utf-8') as user_buy_log:
                for key in user_buy_dict:
                    str_key = str(key)
                    str_value = str(user_buy_dict[key])

                    print(str_key, str_value)
                    user_buy_log.writelines(str_key + ":" + str_value + "\n")

            print("-----Your cart list-----")
            # 退出时，显示购买的商品和余额
            for i in cart:
                print(i)
            print("Your balance: ", salary_dict[username])
            print("-----END-----")
            break
        else:
            print("Options you input is wrong, please input again")

else:
    print("User or password is not correct...")