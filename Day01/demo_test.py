#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import time

class to_test(object):
    def __init__(self):
        self.name = 'alex'

    def change(self, name):
        self.name = name

    def to_print(self):
        print("name:", self.name)

if __name__ == '__main__':
    name = input(">>> ").strip()
    test = to_test()
    test.to_print()
    test.change(name)
    test.to_print()
    time.sleep(30)
