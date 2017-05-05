#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: PanFei Liu

import getpass

dict_user = {}
dict_sign = {}
with open("user_password.txt") as dict_user_password:
    for up in dict_user_password.readlines():
        user_passwd = up.split(":")
        user = user_passwd[0]
        passwd = user_passwd[1].rstrip()
        dict_user[user] = passwd
print("dict:", dict_user)

while True:
    username = input("username: ")
    password = input("password: ")

    if username in dict_user.keys():
        if dict_user[username] == password:
            print("Welcome: ", username)
            break
        elif username not in dict_sign.keys():
            dict_sign[username] = 1
            print("The user or password is not correct!")
        elif dict_sign[username] < 3:
            tmp = dict_sign[username]
            dict_sign[username] = tmp + 1
            print("The user or password is not correct!")
        else:
            print("the user %s is locked!"% username)
            result = input("Do uou need to reset the login?(Y/N)")
            while result not in ("YyNn"):
                result = input("Do uou need to reset the login?(Y/N)")
            if result in "Yy":
                dict_sign[username] = 0
            else:
                print("-----END-----")
                break
    else:
        print("The user does not exist!")


