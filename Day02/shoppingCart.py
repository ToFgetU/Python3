#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PanFei Liu

product_list = [
    ('Iphone', 5800),
    ('华为荣耀', 5500),
    ('三星', 3300),
    ('小米', 1999)
]
cart = []
salary = input("Input your salary: ")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("Please choose the items what you want >>> ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice]
                if p_item[1] < salary:
                    salary -= p_item[1]
                    cart.append(product_list[user_choice])
                else:
                    print("Your balance \033[31;1m%s\033[0m is insufficient..."% salary)
        elif user_choice in "qQ":
            print("-----cart list-----")
            for i in cart:
                print(i)
            print("Your balance: ")
            print("exit...")
            exit()
        else:
            print("invalid option")
