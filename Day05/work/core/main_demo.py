#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import re
from core import staff_do

def run():
    """运行程序主入口"""
    while True:
        sql_windows = ''.join("SQL操作窗口").center(100, '-')
        sql_retrieve = ''.join("SQL查询窗口").center(100, '-')
        sql_end = ''.join("SQL结束底线").center(100, '-')
        print(sql_windows) #分割线
        sql_str = input(' SQL > ')
        sql_keywords = sql_str.strip().split(" ")

        """
        #select * from staff_table
        #select name,age from staff_table where age > 22
　　    #select * from staff_table where dept = "IT"
        #select * from staff_table where enroll_date like "2013"
        """
        if sql_keywords[0].lower() == 'select' and len(sql_keywords) >= 4:
            if len(sql_keywords) == 9:
                sql_keywords[7] = sql_keywords[7] + ' ' + sql_keywords[8]
                sql_keywords.pop()
            if  sql_keywords[2].lower() == "from" \
                and sql_keywords[3] == "staff_table" and len(sql_keywords) == 4:
                staff = staff_do.staff_read()
            elif sql_keywords[2].lower() == "from" \
                and sql_keywords[3] == "staff_table" and len(sql_keywords) > 4:
                if len(sql_keywords) < 8:
                    print("\033[41;1m输入的格式有误。。。\033[0m")
                    continue
                if sql_keywords[6] not in ">=<=like":
                    print("\033[41;1m输入的格式有误。。。\033[0m")
                    continue
                elif sql_keywords[5].lower() not in ["name", "age", "phone", "dept", "enroll_date"]:
                    print("\033[41;1m输入的格式有误。。。\033[0m")
                    continue
                else:
                    sql_keywords[5] = sql_keywords[5].lower()
                    if sql_keywords[5] == "age":
                        if sql_keywords[7].isdigit():
                            sql_keywords[7] = int(sql_keywords[7])
                        else:
                            print("\033[41;1m输入的格式有误。。。\033[0m")
                            continue
                    else :
                        tmp_str = sql_keywords[7]
                        sql_keywords[7] = tmp_str[1:-1]
                    staff = staff_do.staff_retrieve(sql_keywords[5], sql_keywords[6], sql_keywords[7])
            else:
                print("\033[41;1m输入的格式有误。。。\033[0m")
                continue

        #insert into staff_table values ("Alice Li", 27, "13545677654", "IT", "2017-05-15")
        elif sql_keywords[0].lower() == 'insert':
            temp = re.search(r'\([^()]+\)', sql_str).group()
            temp = eval(temp)
            name = temp[0]
            age = temp[1]
            phone = temp[2]
            dept = temp[3]
            enroll_date = temp[4]
            staff_do.staff_create(name=name, age=age, phone=phone, dept=dept, enroll_date=enroll_date)
        #delete from table where name = 'Alice Li'
        #delete from table where staff_id = 5
        elif sql_keywords[0].lower() == 'delete':
            if len(sql_keywords) == 8:
                sql_keywords[6] = sql_keywords[6] + ' ' + sql_keywords[7]
                sql_keywords.pop()
                tmp_str = sql_keywords[6]
                sql_keywords[6] = tmp_str[1:-1]
            delete_str = sql_keywords[6]
            staff_do.staff_delete(delete_str)
        #update staff_table set dept = "Market" where dept = "IT"
        elif sql_keywords[0].lower() == 'update':
            selection = sql_keywords[7]
            tmp_str = sql_keywords[9]
            sql_keywords[9] = tmp_str[1:-1]
            value = sql_keywords[9]
            update_selection = sql_keywords[3]
            tmp_str = sql_keywords[5]
            sql_keywords[5] = tmp_str[1:-1]
            update_value = sql_keywords[5]
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
        else:
            print("\033[41;1m输入的格式有误。。。\033[0m")
            continue

        print(sql_retrieve) #分割线
        if sql_keywords[0].lower() == 'select':
            count = 0
            if sql_keywords[1] == '*':
                print("\033[44;1m\033[32;1mstaff_id\tname\t\tage\t\tphone\t\t\tdept\tenroll_date\033[0m\033[0m")
                for key, value in staff.items():
                    count += 1
                    print('\t' + key + '\t\t', end='')
                    for k, v in value.items():
                        print(str(v) + '\t\t', end='')
                    print()
            else:
                field = sql_keywords[1].split(',')
                for f in field:
                    print("\033[44;1m\033[32;1m" + f + "\t\t", end = '' + "\033[0m\033[0m")
                print()
                for key, value in staff.items():
                    count += 1
                    for k, v in value.items():
                        if k in field:
                            print(str(v) + '\t\t', end='')
                    print()
            print("\n共查到数据: \033[32;1m%s\033[0m 条"% count)
        print(sql_end + "\n") #分割线
        change = input("是否重新查询(输入任意键继续，退出:exit):")
        if change.lower() == 'exit':
            print("拜拜。。。")
            break
        else:
            pass
