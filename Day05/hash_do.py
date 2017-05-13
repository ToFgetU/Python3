#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import hashlib

# ######## md5 ########

hash = hashlib.md5()
hash.update(b'admin')
print(hash.hexdigest())

data = "你好"
hash.update(data.encode(encoding='utf-8'))
print("\033[32;1mutf-8\033[0m:", hash.hexdigest())
hash.update(data.encode(encoding='gbk'))
print("\033[32;1mgbk\033[0m:", hash.hexdigest())

# ######## sha1 ########

hash = hashlib.sha1()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha384 ########

hash = hashlib.sha384()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update(b'admin')
print(hash.hexdigest())