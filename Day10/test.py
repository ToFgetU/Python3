#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu
sum = 0
n = 1
while n < 1000:
    sum += n * (1000 - (n-1))/2
    n += 2

print(sum)
