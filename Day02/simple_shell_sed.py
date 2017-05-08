#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

f = open("data/shell.txt", "r", encoding="utf-8")
f_new = open("data/shell_new.txt", "w", encoding="utf-8")
old_line = input("输入你要替换的内容: ")
new_line = input("输入你替换后的内容: ")

for line in f:
    if old_line in line:
        line = line.replace(old_line, new_line)
    f_new.writelines(line)
    f.flush()

f_new.close()
f.close()
