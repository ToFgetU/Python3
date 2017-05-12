#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import time, datetime

print(time.time())

t = time.strptime("2017-05-12 12:00", "%Y-%m-%d %H:%M")
print(t)
t1 = time.mktime(t)
print(t1)
t2 = time.strftime("%Y_%m_%d %H:%M", t)
print(t2)

now = datetime.datetime.now()
print(now)

print(''.join("random").center(60, "-"))
import random
import string

checkcode = ''
for i in range(4):
    cur = random.randrange(0, 4)
    if cur != i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    checkcode += str(tmp)
print(checkcode)

print(string.ascii_letters)
r = string.ascii_letters + string.digits
print(random.sample(r, 4))

print(''.join("json").center(60, "-"))
import json,pickle

dict1 = {
    "name":"alex",
    "age":22
}
fd = open("text.txt", "w")

fd.write(json.dumps(dict1))

fd.close()

fl = open("text.txt", "r")
data = json.loads(fl.read())
print(type(data))
print(data)

print(''.join("shelve").center(60, "-"))