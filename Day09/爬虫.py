#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

from urllib import request
import gevent, time
from gevent import monkey
# 把当前程序的所有IO操作给单独的做上标记
monkey.patch_all()

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/', 'https://www.yahoo.com/', 'https://github.com/']

time_start = time.time()
for url in urls:
    f(url)
print('同步cost', time.time()-time_start)

async_time_start = time.time()
gevent.joinall([gevent.spawn(f, 'https://www.python.org/'),
                gevent.spawn(f, 'https://www.yahoo.com/'),
                gevent.spawn(f, 'https://github.com/')])
print('异步cost', time.time()-async_time_start)