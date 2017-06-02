#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu


#闭包问题，只需要给i传值 并可解决
bar = [lambda x, i = i : i + x for i in range(10)]
val = bar[6](100)
print(val)

