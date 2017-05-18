#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import json

shopping = {
    '高配组装机': 6188,
    '联想笔记本': 5688,
    'Iphone 7': 6388,
    '海尔冰箱': 2788,
    '奥克斯空调': 1999,
    'Python程序开发指南': 69,
    '玩具电动车': 188,
    '捷安特自行车': 2299,
    '固态硬盘': 399
}

with open("shopping.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(shopping, indent=4, separators=(',', ':')))

f = open("shopping.json", 'r', encoding='utf-8')
ss = json.loads(f.read())
print("shopping", ss)

atm_user = {
    'admin': {
            'password': 'abc123',
            'is_admin': 1
    },
    'test': {
        'password': '123',
        'credit': 15000,
        'acc_frozen': 0,
        'is_admin': 0
    },
    'alice': {
        'password': 'abc',
        'credit': 15000,
        'acc_frozen': 0,
        'is_admin': 0
    }
}

shopping_user = {
    'test': {
        'password': '123'
    },
    'alice': {
        'password': 'abc'
    }
}

with open("atm_user.json", 'w', encoding='utf-8') as f, open("shopping_user.json", 'w', encoding='utf-8') as f2:
    f.write(json.dumps(atm_user, indent=4, separators=(',', ':')))
    f2.write(json.dumps(shopping_user, indent=4, separators=(',', ':')))

f = open("atm_user.json", 'r', encoding='utf-8')
ss = json.loads(f.read())
print("atm_user", ss)

f2 = open("shopping_user.json", 'r', encoding='utf-8')
ss2 = json.loads(f2.read())
print("shopping_user", ss2)