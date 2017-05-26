#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import re
import string
from core import arithmetic

def processing(s):
    """运算处理模块，对输入的字符串进行格式化处理"""
    operation_pieces = {}

    for i in string.ascii_lowercase:
        if re.search(r'\([^()]+\)', s):
            r = re.search(r'\([^()]+\)', s).group() #对匹配到的字符串进行分组 正则表达式中，group（）用来提出分组截获的字符串，（）用来分组
        else:
            operation_pieces[i] = s
            # print("======")
            break

        if r:
            s = re.sub(r'\([^()]+\)', i, s, 1)
            operation_pieces[i] = r
            print("\t运算步骤:", s)
        else:
            # print("---")
            break
    # print(operation_pieces)
    print("计算ING========")
    #对碎片进行分步计算
    result_pieces = {}
    for key in string.ascii_lowercase:
        # print(key)
        values = operation_pieces[key]
        cal_dict = {}  # 获取字符串并对字符串相连数字进行重组
        cal_str = []  # 保存数字
        cal_ope = []  # 保存算术符号
        ss = ''  # 作用拼接字符串
        # print(key, values)
        if '(' in values:
            values = values[1:-1].strip()
        values = list(values)
        for index, v in enumerate(values):
            # print("---------> ", index, v)
            if v.replace('.', '', 1).isdigit() or v in string.ascii_letters:
                cal_dict[index] = v
            else:
                if v in "+-*/":
                    cal_ope.append(v)
        # print(cal_dict)
        if cal_dict:
            count = 0
            for num in range(max(cal_dict)+1):
                # print(num)
                if num in cal_dict.keys():
                    if cal_dict[num].replace('.', '', 1).isdigit(): #判断整数及小数
                        ss = ss + cal_dict[num]
                        count = 0
                        if num == max(cal_dict):
                            cal_str.append(int(ss))
                    else:
                        # print(cal_dict)
                        # print(result_pieces)
                        # print(cal_str)
                        cal_str.append(result_pieces[cal_dict[num]])
                        count += 1
                else:
                    if count == 0:
                        count += 1
                        if num == 0:
                            continue
                        cal_str.append(int(ss))
                        ss = ''
                    else:
                        continue
            if values[0].replace('.', '', 1).isdigit():
                pass
            else:
                if values[0] == '-':
                    x = cal_ope[0] + str(cal_str[0])
                    cal_str[0] = int(x)
                    del cal_ope[0]
                    # print(x)
        else:
            pass

        # print(cal_str)
        # print(cal_ope)

        def calculate(t):
            """判断优先级，然后进行运算"""
            index = cal_ope.index(t)
            if t == '*':
                result = arithmetic.mul(cal_str[index], cal_str[index + 1])
            elif t == '/':
                result = arithmetic.div(cal_str[index], cal_str[index + 1])
            elif t == '+':
                result = arithmetic.add(cal_str[index], cal_str[index + 1])
            else:
                result = arithmetic.sub(cal_str[index], cal_str[index + 1])
            del cal_ope[index]
            del cal_str[index + 1]
            cal_str[index] = result

        while cal_ope:
            if '*' in cal_ope and '/' in cal_ope:
                if cal_ope.index('*') < cal_ope.index('/'): #index 越小优先级越高
                    calculate('*')
                else:
                    calculate('/')
            elif '*' in cal_ope:
                calculate('*')
            elif '/' in cal_ope:
                calculate('/')
            elif '*' not in cal_ope and '/' not in cal_ope and ('+' in cal_ope or '-' in cal_ope):
                while cal_ope:
                    calculate(cal_ope[0])
            else:
                break

            result_pieces[key] = cal_str[0]
        if key == max(operation_pieces):
            break
        # print("result_pieces: ", result_pieces)
            # print(max(result_pieces.keys()))
            # print(cal_dict)
    final_result = result_pieces[max(result_pieces.keys())]
    return final_result


# s = '1 - 2 *(3 - 2)'
# print(eval(s))
# tp = processing(s)
# print(tp)