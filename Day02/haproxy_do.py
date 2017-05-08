#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

def open_file(mode):
    """打开文件"""
    h_file =  open("data/haproxy.cfg", mode, encoding="utf-8")
    return h_file

def retrieve(str):
    """查询"""
    f = open_file('r')
    str = "backend " + str
    count = 0
    for line in f:
        if str in line and line[0] == 'b':
            count += 1
            print(line.rstrip())
        elif count == 1:
            print(line)
            count = 0
        else:
            pass
    f.close()


def create(string):
    """新增"""
    dict_str = eval(string)
    print(dict_str)
    f = open_file('r+')
    count = 0 #是否已经存在配置的标记
    for line in f:
        if dict_str["bakend"] in line and count == 0:
            #print(dict_file["bakend"] )
            print("Configuration has been... ")
            count = 1


    if count == 0:
        str_bakend = "bakend " + dict_str["bakend"] + "\n"
        str_record = "\t\tserver " + dict_str["record"]["server"]\
                     + " weight " + str(dict_str["record"]["weight"])\
                     + " maxconn " + str(dict_str["record"]["maxconn"])

        # print(str_bakend, str_record)
        f.writelines("\n\n")
        f.writelines(str_bakend)
        f.writelines(str_record)
        f.close()
        print("Add success ...")


def haproxy_do():
    """增删查操作"""
    print("""
    -> 1 search
    -> 2 add
    -> 3 delete
    """)
    name = input("What do you want. >>> ")
    if name.isdigit():
        name = int(name)
        if name == 1:
            str = input("--> What do you retrieve. >>> ") #www.oldboy.org
            retrieve(str)
        elif name == 2:
            str = input("--> Input your arg. >>> ")
            create(str)
        elif name ==3:
            pass
        else:
            print("Input is wrong...")
    else:
        print("Input is wrong...")



haproxy_do()

"""
{'bakend': 'haproxy.org', 'record':{'server': '100.1.7.8', 'weight': 20, 'maxconn': 3000}}
"""
