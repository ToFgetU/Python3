#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import re
def processing(s):
    """运算处理模块，对输入的字符串进行格式化处理"""
    cal_string = re.search(r'\([^()]+\)', s).group()
    cal_string = cal_string[1:-1].rstrip()
    cal_string = list(cal_string)
    print(cal_string)
    cal_dict = {} # 获取数字并对其格式化
    cal_str = [] # 保存数字
    cal_ope = [] # 保存算术符号
    ss = '' # 作用拼接字符串

    for index, value in enumerate(cal_string):
        # print(index, value)
        if value.isdigit():
            cal_dict[index] = value
        else:
            if value in "+-*/":
                cal_ope.append(value)
    count = 0


    for num in range(max(cal_dict)+1):
        # print(num)
        if num in cal_dict.keys():
            ss = ss + cal_dict[num]
            count = 0
            if num == max(cal_dict):
                cal_str.append(int(ss))
        else:
            if count == 0:
                count += 1
                if num == 0:
                    continue
                cal_str.append(int(ss))
                ss = ''
            else:
                continue

    if cal_string[0].isdigit():
        pass
    else:
        x = cal_ope[0] + str(cal_str[0])
        cal_str[0] = int(x)
        del cal_ope[0]
        print(x)

    if '*' in cal_ope and  "/" in cal_ope:
        pass
    elif '*' in cal_ope:
        pass
    elif "/" in cal_ope:
        cal_ope


    print(cal_str)
    print(cal_ope)




s = '1 - 2 * ( (60-30 + (-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
processing(s)