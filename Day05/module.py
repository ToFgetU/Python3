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
fd = open("text.txt", "a")

fd.write(json.dumps(dict1))
fd.close()

fl = open("text.txt", "r")
data = json.loads(fl.read())
print(type(data))
print(data)

print(''.join("shelve").center(60, "-"))


print(''.join("插入").center(60, '-'))
import json


dict1 = {
    "1": {
        'name':'Alex Li',
        'age':22,
        'phone':'13651054608',
        'dept':'IT',
        'enroll_date':'2013-04-01'
    },
    "2": {
        'name':'Jack Wang',
        'age':30,
        'phone':'13304320533',
        'dept':'HR',
        'enroll_date':'2015-05-03'
    },
    "3": {
        'name':'Raln Liu',
        'age':25,
        'phone':'1383235322',
        'dept':'Sales',
        'enroll_date':'2016-04-22'
    },
    "4": {
        'name':'Mack Cao',
        'age':40,
        'phone':'1356145343',
        'dept':'HR',
        'enroll_date':'2009-03-01'
    }
}



f = open("work/data/staff.json", "w", encoding='utf-8')

f.write(json.dumps(dict1, indent=4, separators=(',', ':')))
# print(json.dumps(dict1, indent=4, separators=(',', ':')))
f.close()