#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    s = main.Handler()
    s.start()