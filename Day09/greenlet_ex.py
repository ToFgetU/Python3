#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

from greenlet import greenlet

def greenlet_1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def greenlet_2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(greenlet_1)
gr2 = greenlet(greenlet_2)
gr1.switch()