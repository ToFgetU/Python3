#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import os
import json

def staff_read():
    """获取员工信息表"""
    print("---")
    BASE_DIR = os.path.dirname(__file__)
    # print(BASE_DIR)
    staff_file = open(os.path.join(BASE_DIR, "../data/staff.json"), "r", encoding="utf-8")
    # print("-->", staff_file)
    staff_data = json.loads(staff_file.read())
    # print(staff_data)
    staff_file.close()
    return staff_data

def staff_retrieve(*args):
    """对员工表进行查询，支持模糊查询，判断查询"""
    staff = staff_read()
    count = 0
    r_staff = []
    for key, value in staff.items():
        # print(key, value)
        if args[0] in value.keys():
            if isinstance(args[2], int): #判断是否是数字，如果是数字，进行判断查询
                if args[1] == ">":
                    if value[args[0]] > args[2]:
                        count += 1
                        r_staff.append(staff[key])
                elif args[1] == ">=":
                    if value[args[0]] >= args[2]:
                        count += 1
                        r_staff.append(staff[key])
                elif args[1] == "<":
                    if value[args[0]] < args[2]:
                        count += 1
                        r_staff.append(staff[key])
                elif args[1] == "<=":
                    if value[args[0]] <= args[2]:
                        count += 1
                        r_staff.append(staff[key])
                elif args[1] == "=":
                    if value[args[0]] == args[2]:
                        count += 1
                        r_staff.append(staff[key])
                else:
                    print("\033[41;1m输入的格式有误。。。\033[0m")
                    break
            else:
                if args[1] == "=":
                    if value[args[0]] == args[2]:
                        count += 1
                        r_staff.append(staff[key])
                elif args[1] == "like": #模糊查询
                    if args[2] in value[args[0]]:
                        count += 1
                        r_staff.append((staff[key]))
                else:
                    print("\033[41;1m输入的格式有误。。。\033[0m")
        else:
            print("\033[41;1m输入的格式有误。。。\033[0m")
    # print("--> ", count, r_staff)
    return count, r_staff


def staff_create(**kwargs):
    """新增员工数据，如果phone重复，这不添加"""
    staff = staff_read()
    max_id = str(int(max(staff.keys())) + 1)
    # print(max_id)
    #print(kwargs)

    sign = 0 #标记phone是否重复
    for key, value in staff.items():
        if kwargs["phone"] == value["phone"]:
            sign += 1
            break
        else:
            pass

    if sign == 0:
        staff[max_id] = kwargs
        with open("../data/staff.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(staff, indent=4, separators=(',', ':')))
            print("添加成功")
    else:
        print("The phone is already in the staff table.")

def staff_delete(*args):
    """根据用户名或者 staff_id进行删除"""
    staff = staff_read()
    max_id = int(max(staff.keys()))

    sign = 0 #标记要删除的数据是否存在
    if args[0].isdigit():
        num = int(args[0])
        if max_id >= num:
            sign += 1
            staff_id = args[0]
        else:
            print("你输入的 \033[31;1mstaff_id: %s\033[0m 不存在"% args[0])

    else:
        for key, value in staff.items():
            if args[0] == value["name"]:
                sign += 1
                staff_id = key
                break
    if sign == 0:
        print("你输入的 \033[31;1mname: %s\033[0m 不存在" % args[0])
    else:
        print("开始删除 %s "% staff[staff_id])
        del staff[staff_id]
        with open("../data/staff.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(staff, indent=4, separators=(',', ':')))
        print("删除成功")

def staff_update(**kwargs):
    """根据修改条件进行修改"""
    staff = staff_read()
    dict_values = kwargs.values()
    staff_values = []
    for i in dict_values:
        staff_values.append(i)
    print(staff_values)

    for key, value in staff.items():
        # print(key, value)
        if value[staff_values[0]] == staff_values[1]:
            if staff_values[2] == "age":
                staff[key][staff_values[2]] = int(staff_values[3])
            else:
                staff[key][staff_values[2]] = staff_values[3]
        else:
            pass

    with open("../data/staff.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(staff, indent=4, separators=(',', ':')))
        print("更新成功")
    # for k in staff:
    #     print("\t", k, staff[k])
