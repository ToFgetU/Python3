#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import staff_do_bak

def run():
    """运行程序主入口"""
    while True:
        print("\n")
        print(''.join("操作菜单").center(40, '-'))
        print("""
    0 全表查询
    1 查询
    2 新增
    3 修改
    4 删除
        """)

        num = input("请选择你要的操作(Q/q 退出): ")
        if num.isdigit():
            num = int(num)
            if num == 1:
                r_string = input("请输入要查询的内容(格式:dept = IT/age > 22/enroll_date like 2013): ")
                string_list = r_string.split(" ")
                if len(string_list) == 4:
                    string_list[2] = string_list[2] + ' ' + string_list[3]
                    string_list.pop()
                    print(string_list)
                if len(string_list) != 3:
                    print("\033[41;1m输入的格式有误。。。\033[0m")
                    continue
                else:
                    if string_list[1] not in ">=<=like":
                        print("\033[41;1m输入的格式有误。。。\033[0m")
                        continue
                    elif string_list[0].lower() not in ["name", "age", "phone", "dept", "enroll_date"]:
                        print("\033[41;1m输入的格式有误。。。\033[0m")
                        continue
                    else:
                        string_list[0] = string_list[0].lower()
                        if string_list[0] == "age":
                            if string_list[2].isdigit():
                                string_list[2] = int(string_list[2])
                            else:
                                print("\033[41;1m输入的格式有误。。。\033[0m")
                                continue
                        staff = staff_do.staff_retrieve(string_list[0], string_list[1], string_list[2])
                        for i in staff[1]:
                            print(i)
                        print("查询数据总共: \033[32;1m%s\033[0m 条"% staff[0])
            elif num == 2:
                name = input("name: ")
                while True:
                    age = input("age: ")
                    if age.isdigit():
                        age = int(age)
                        break
                    else:
                        age = input("输入的不是数字，请重新输入 age: ")
                phone = input("phone: ")
                dept = input("dept: ")
                enroll_date = input("enroll_date(yyyy-mm-dd): ")

                staff_do.staff_create(name=name, age=age, phone=phone, dept=dept, enroll_date=enroll_date)

            elif num == 3:
                selection = input("请选择\033[34;1m待更改\033[0m项(name/age/phone/dept/enroll_date): ")
                value = input("请输入\033[34;1m待更改\033[0m条件(Alice/22/13304320533/Sales):")
                update_selection = input("请选择\033[34;1m更改\033[0m项(name/age/phone/dept/enroll_date): ")
                update_value = input("请输入\033[34;1m更改\033[0m内容(Alice/22/13304320533/Sales):")
                if selection.lower() not in ["name", "age", "phone", "dept", "enroll_date"]:
                    print("\033[41;1m输入的格式有误。。。\033[0m")
                    continue
                elif update_selection.lower() not in ["name", "age", "phone", "dept", "enroll_date"]:
                    print("\033[41;1m输入的格式有误。。。\033[0m")
                    continue
                else:
                    selection = selection.lower()
                    update_selection = update_selection.lower()
                staff_do.staff_update(selection=selection,
                                      value=value,
                                      update_selection=update_selection,
                                      update_value=update_value)

            elif num == 4:
                delete_str = input("请输入要删除的staff_id 或 name:")
                staff_do.staff_delete(delete_str)
            elif num == 0:
                staff = staff_do_bak.staff_read()
                for k, v in staff.items():
                    print(k, v)
            else:
                print("输入的选择不在操作菜单内。。。")
        elif num in "qQ":
            break
        else:
            print("选择错误。。。")


run()





