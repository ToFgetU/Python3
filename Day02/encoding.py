#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import sys
print(sys.getdefaultencoding()) #环境变量字符集

#python3 中 字符集默认会先转换成 bytes类型
s = "你好" #默认字符集为unicode，与设定的字符集无关，python3默认字符集为unicode
print(s.encode("gbk")) #unicode -> gbk
print(s.encode("gbk").decode("gbk").encode("utf-8")) # unicode -> gbk -> unicode -> utf-8
print(s.encode("gbk").decode("gbk").encode("utf-8").decode("utf-8")) # unicode -> gbk -> unicode -> utf-8->中文显示

def test(name, age = 18, **args):
    print(name)
    print(age)
    print(args)

test('alex', sex='F', age=11, hoddy='dsf')