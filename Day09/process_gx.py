#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

from multiprocessing import Process, Manager
import os

def run(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print('dd', d)
    print('ll', l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))

        p_list = []
        for i in range(10):
            p = Process(target=run, args=(d, l))
            p.start()
            p_list.append(p)

        for r in p_list:
            r.join()

        print(d)
        print(l)