#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: PanFei Liu
import sys
print("Hello World!")

a, b = 2, 3
c = a if b > a else None

print(a, b, c)

collection_1 = set([1, 2, 3])
collection_2 = set([1, 3, 5])

print(collection_1.difference(collection_2))
print(collection_1.intersection(collection_2))
print(collection_1.union(collection_2))
print(collection_1.symmetric_difference(collection_2))

# sum = 0
# for i in range(1, 101):
#     if i%2:
#         sum += i
#     else:
#         sum -= i
# print(sum)
sum = 0
count = 1
while count <= 100:
    if count%2:
        sum += count
        count += 1
    else:
        sum -= count
        count += 1

print(sum)