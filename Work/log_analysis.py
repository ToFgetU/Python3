#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu


file_list = []
info_list = []


with open('tmp.log','r') as f:
    for k, line in enumerate(f):
        if k == 0:
            pass
        file_list.append(line)
file_list.pop()

for key, line in enumerate(file_list):
    tmp = line.split()
    app = tmp[8].split('/')
    h_app = app[0].split('_')
    temp = tmp[17].split('"')
    info_list.append(('%s_%s' % (h_app[0], app[1]), tmp[10], temp[1]))

app_dir = {}

count = 0
for i in info_list:
    if i[0] in app_dir:
        if i[1] in app_dir[i[0]]:
            app_dir[i[0]][i[1]] += 1
        else:
            app_dir[i[0]][i[1]] = 1
    else:
        app_dir[i[0]] = {i[1]: 1}

for k, v in app_dir.items():
    print(k, v)