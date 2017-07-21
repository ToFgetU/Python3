#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import cx_Oracle

db = cx_Oracle.connect('dev/dev@192.168.128.131:1521/orcl')
print(db.version)