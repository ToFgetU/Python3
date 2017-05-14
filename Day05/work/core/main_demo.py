#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import staff_do

while True:
    sql_windows = ''.join("SQL操作窗口").center(100, '-')
    sql_retrieve = ''.join("SQL查询窗口").center(100, '-')
    sql_end = ''.join("SQL结束底线").center(100, '-')
    print(sql_windows)
    sql_str = input(' SQL > ')
    print(sql_retrieve)
    print(sql_end)

    break