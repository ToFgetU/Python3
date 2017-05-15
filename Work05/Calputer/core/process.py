#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import re
def processing():
    s = '1 - 2 * ( (60-30 + -8 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    cal_string = re.search(r'\([^()]+\)', s).group()
    print(cal_string)
    cal_string = cal_string[1:-1]
    cal_string = list(cal_string)
    cal_str = []
    x = ''


processing()