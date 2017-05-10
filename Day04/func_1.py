#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

x = 0
def grandpa():
    x = 1
    def dad():
        x=2
        def son():
            x=3
            print(x)
        son()
    # dad()
grandpa()


res = print("nothing")
print(res)