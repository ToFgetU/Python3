#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

class F1:
    def __init__(self, n):
        self.N = n
        print('F1')

class F2:
    def __init__(self, arg1):
        self.a = arg1
        print('F2')
    def func(self):
        print(11)

class F3:
    def __init__(self, arg2):
        self.b = arg2
        print('F3')
    def p(self):
        return self.b

o1 = F1('alex')
o2 = F2(o1)
o3 = F3(o2)
r1 = o3.p()
print(r1)

r2 = r1.func()
print('111', r2)

# 通过 o3 获取 alex
print(o3.b.a.N)