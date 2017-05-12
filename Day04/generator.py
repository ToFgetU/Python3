#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

a = (i*2 for i in range(10))
print(a)
print(a.__next__())
print("-------->")
print(a.__next__())
print("-------->")
for i in a:
    print(i)

print("=========")
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b
        n += 1

    return "done"

g = fib(5)
while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
