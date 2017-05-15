#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu


list1 = ['alex', 'eric', 'rain']
print('_'.join(list1))
str1 = list1[0] + "_" + list1[1] + "_" + list1[2]
print(str1)



tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])

print(tu)

#使用while循环实现输出 1-100 内的所有奇数

# count = 1
# while count <= 100:
#     if count%2:
#         print(count)
#         count += 1
#     else:
#         count += 1
#         continue

#使用while循环实现输出2 - 3 + 4 - 5 + 6 ... + 100 的和

# count = 2
# sum = 0
# while count <= 100:
#     if count%2:
#         sum = sum - count
#         count += 1
#     else:
#         sum = sum + count
#         count += 1
# print(sum)
#
# s = "你是风儿%s我是沙%s"
# n = s%  ('僧')
# print(n)

list1 = [1,2,3,4,1,3,2]
print(list1.index(1))