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