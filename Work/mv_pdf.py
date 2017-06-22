#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import time

print(time.localtime())

localhosttime = time.asctime(time.localtime(time.time()))
print(localhosttime)

localhosttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(localhosttime)

