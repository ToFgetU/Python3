#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu


#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

# 装饰器
# def auth(func):
#     def wapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wapper
#
#
#
# @auth
# def login():
#     print("这是登入页面")
#
#
# login()
#
#
# import time
#
# def auth1(mode):
#     def outwapper(func):
#         def wapper(*args, **kwargs):
#             start_time = time.time()
#             if mode == 'local':
#                 rec = func(*args, **kwargs)
#                 return rec
#
#             else:
#                 pass
#             stop_time = time.time()
#             print("共花费时间：", (stop_time-start_time))
#         return wapper
#     return outwapper
#
#
# @auth1(mode='local')
# def login(name):
#     time.sleep(3)
#     print("这是登入页面", name)
#
# login('test')


# #生成器 带 yield 关键字
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1


#迭代器 用 next 或者 iter 方法进行迭代
# import time
#
# def consumer(name):
#     print("%s 准备吃包子啦"%  name)
#     while True:
#         baozi = yield
#
#         print("客户 %s 准备吃第[%s]个包子"% (name, baozi))
#
# def producer(max):
#     c1 = consumer('A')
#     c2 = consumer('B')
#
#     c1.__next__()
#     c2.__next__()
#
#     print("准备做包子啦")
#     for i in range(max):
#         time.sleep(1)
#         print("第%s个包子"% i)
#         c1.send(i+1)
#         c2.send(i+1)
#
# producer(3)


#1*2+3*4+5*6+7*8...+99*100

# def mul(x, y):
#     """乘法"""
#     return x * y
#
# def math():
#     jishu = []
#     oushu = []
#     to_add = []
#     result = 0
#     for i in range(101):
#         if i == 0:
#             continue
#         elif i%2:
#             jishu.append(i)
#         else:
#             oushu.append(i)
#
#     for j in range(len(jishu)):
#         to_add.append(mul(jishu[j], oushu[j]))
#
#     for m in to_add:
#         result += m
#     print(result)
#
# math()
