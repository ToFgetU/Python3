#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu


class F1:
    def __init__(self):
        print('F1')

    def a1(self):
        print('F1a1')

    def a2(self):
        print('F1a2')

class F2(F1):
    def __init__(self):
        print('F2')

    def a1(self):
        self.a2()
        print('F2a1')

    def a2(self):
        print('F2a2')

class F3(F2):
    def __init__(self):
        print('F3')

    # def a1(self):
    #     print('F3a1')

    def a2(self):
        print('F3a2')

obj = F3()
obj.a1()

# 执行结果
 # F3a2  F2a1