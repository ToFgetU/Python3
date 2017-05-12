#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu
from collections import Iterable,Iterator

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

print("------")
def test1():
    print("in the test1")

def test2(func):
    func()
    print("in the test2")
    return func

def test3():
    str = test2(test1)
    print(str)
    print("in the test3")
test3()
print("--------")

res = filter(lambda n:n>5, range(10))
print(type(res))
print(isinstance(res, Iterator))
for i in res:
    print(i)