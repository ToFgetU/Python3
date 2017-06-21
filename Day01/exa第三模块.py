# #!/usr/bin/env python3
# # -*- coding:utf-8 -*-
# # Author: Panfei Liu
#
#
# 知识点概要：
#     - 面向对象
#     - 类和对象
#     - 类成员
#     - 类继承
#     - 成员修饰符
#     - 特殊成员
#
# 考察题目：
#     1. 简述类、对象、实例化是什么鬼？
#
#     2. 简述构造方法和析构方法
#
#     3. 类和对象在内存中的关系是怎样的？请画图说明
#
#     4. 面向对象适用场景？
#         - 多个方法使用共同的参数
#         - 根据同一个模板创建对象
#
#     5. 面向对象编程中类和对象的成员都有那些？
#         - 字段（静态字段、普通字段）
#         - 方法（静态方法、类方法、普通方法）
#         - 属性
#
#     6. 以下面向成员那些属于类那些属于对象？
#         - 字段（静态字段、普通字段）
#         - 方法（静态方法、类方法、普通方法）
#         - 属性
#
#     7. 面向对象三大特性以及在Python中如体现？
#
#     8. Python多继承应用，看代码，写答案：
#         class A(object):
#             def request(self):
#                 print('A.request')
#
#             def finish(self):
#                 print('A.finish')
#
#         class C(A):
#             def request(self):
#                 self.process()
#                 print('C.request')
#
#             def finish(self):
#                 print('C.finish')
#
#         class B(object):
#             def request(self):
#                 print('B.request')
#
#             def process(self):
#                 print('B.process')
#                 self.finish()
#
#             def finish(self):
#                 print('B.finish')
#
#         class D(C, B):
#             pass
#
#         obj = D()
#         obj.request()
#
#         请书写输出内容：
#
#     9. 成员修饰符中的私有和共有通过双下划线来区分，私有成员的特点？
#
#     10. 看代码，书写输出内容：
#         class B:
#             def __conn(self):
#                 print('conn')
#
#
#         class A(B):
#             def request(self):
#                 self.__conn()
#
#
#         obj = A()
#         obj.request()
#
#     11. 特殊成员作用以及如何触发：
#         a. __init__
#         b. __call__
#         c. __str__
#         d. __dict__
#         e. __setitem__  __getitem__ __delitem__
#         f. __new__
#
#     12. 查看代码，书写结果：
#         class A:
#             def __init__(self, name,age):
#                 self.name = name
#                 self.age = age
#
#         class B:
#
#             def __init__(self,a):
#                 self.a = a
#
#             def func(self):
#                 print(self.a.name)
#
#         class C:
#
#             def __init__(self,b):
#                 self.b = b
#
#             def process(self):
#                 return self.b
#
#         objA = A('alex',18)
#         objB = B(objA)
#         objC = C(objB)
#         r1 = objC.process()
#         print(r1)
#
#         r2 = r1.func()
#         print(r2)
#         请输出结果：