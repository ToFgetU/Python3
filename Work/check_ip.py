#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

ip = dict()

def ip_count():
    global ip
    with open('F:/tmp.log', 'r') as f:
        for line in f:
            # print(line)
            line = line.split()
            tmp_ip = line[7].split(':')[0]
            # print(tmp_ip)
            if tmp_ip in ip:
                ip[tmp_ip] += 1
            else:
                ip[tmp_ip] = 1
    # 对字典进行排序 生成list
    sorted_ip = sorted(ip.items(), key=lambda x: x[1], reverse=True)
    print(sorted_ip)
    with open('ip_count.txt', 'w') as f:
        for v in sorted_ip:
            line = '%s 访问次数： %s \n' % (v[0], v[1])
            f.write(line)


ip_count()
