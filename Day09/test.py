#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

print('test')
print('hello')

# import pickle,json
#
# info = '123123'
#
# p = pickle.dumps(info)
#
# print(info, p)
#
# p1 = pickle.loads(p)
# print(p1)
#
# # with open('test.txt', 'wb') as f:
# #     p = pickle.dump(info, f)
#
#
# with open('test.txt', 'wb') as f:
#     p = pickle.dumps(info)
#     f.write(p)

a = [1,2,3,4,5]
tmp = []
for i in range(len(a)):
    tmp.append(a.pop())

a = tmp
print(a)

