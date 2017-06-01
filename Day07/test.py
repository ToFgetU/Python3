#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

bar = [lambda x: i + x for i in range(10)]
val = bar[7](1)
print(val)