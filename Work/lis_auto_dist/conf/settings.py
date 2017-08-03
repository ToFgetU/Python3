#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

HOST_IP = """
localhost
10.28.31.181
10.28.31.182
10.28.31.183
10.28.31.184
10.28.31.185
10.28.31.186
10.28.31.187
10.28.31.188
10.28.31.189
10.28.31.190
10.28.31.191
10.28.31.192
10.28.31.193
10.28.31.199
10.28.32.61
10.28.32.62
10.28.32.63
10.28.32.64
10.28.32.65
10.28.32.66
10.28.32.67
10.28.32.68
"""

HOST = HOST_IP.split()

import logging
import time

now_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
logfile = '%s.log' % now_time
print(now_time)
# create logger
logger = logging.getLogger('ATM-LOG')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
fh = logging.FileHandler("../logs/%s" % logfile, encoding='utf-8')
fh.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
# ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
# logger.addHandler(ch)
logger.addHandler(fh)
