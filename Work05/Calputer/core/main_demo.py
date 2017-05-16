#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

from core import process

def run():
    cal_string = input("请输入你的算式: ")
    result = process.processing(cal_string)
    print("该算式的结果是: ", result)