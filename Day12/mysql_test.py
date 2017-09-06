#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pymysql

# 创建数据库连接
conn = pymysql.connect(host='192.168.128.133', port=3306, user='root', passwd='mysql', db='learndb')

# 创建游标
cursor = conn.cursor()

# 执行SQL, 并返回数据行数
# effect_row = cursor.execute("insert into user values ('2', 'test', '123')")

cursor.execute("select * from user")
# 获取第一行数据
# row_1 = cursor.fetchone()

# 获取前n行数据
# row_2 = cursor.fetchmany(3)

# 获取所有数据
row_3 = cursor.fetchall()
print(row_3)
# 提交，不然无法保存操作的数据
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()