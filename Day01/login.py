#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import getpass

count = 0
sign = True
while sign:
    file = open("user.txt")
    user_sign = open("user_sign.txt", "w")

    username = input("账户: ")
    password = getpass.getpass("密码: ")

    for up in file.readlines():
        print("up:", up)
        user = up.split(":")
        if username == user[0] and password == user[1].strip():
            print("Welcome:", username)
            sign = False
            break
        elif username == user[0] and password != user[1].strip():
            print("user or password is not correct !")
            count += 1
            if count >= 2:
                user_sign.writelines(user[0])
                break
            break

    for us in user_sign.readlines():
        if username == us:
            print("The user is locked ！")

            sign = False
            break
        user_sign.close()
    file.close()






