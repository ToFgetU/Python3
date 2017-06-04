#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

class A:
    def __init__(self, username, password):
        self._USERNAME = username
        self._PASSWORD = password

    def login(self):
        u = 'test'
        p = 'test'

        if u == self._USERNAME and p == self._PASSWORD:
            return "登入成功"
        else:
            return "登入失败"

t = A('test', '123')
print(t.login())
