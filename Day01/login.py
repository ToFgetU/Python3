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
        if dict_user[username] == password and username not in dict_sign:
            print("Welcome: ", username)
            break
        elif dict_user[username] == password and dict_sign[username] < 2:
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
            result = input("Whether or not to continue?(Y/N)")
            while result not in ("YyNn"):
                result = input("Whether or not to continue?(Y/N)")
            if result in "Yy":
                pass
            else:
                print("-----END-----")
                break
    else:
        print("The user does not exist!")


