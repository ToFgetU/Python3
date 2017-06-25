#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import configparser

config = configparser.ConfigParser()
config.sections()
print(config.sections())

config.read("config.ini")
print(config.sections())

print(config['bitbucket.org']['User'])

if config.has_section("topsecret.server.com"):
    config.set('topsecret.server.com', 'compressionlevel', '5')
    config.write(open('config.ini', 'w'))

print(''.join("分割线").center(60, '-'))
for key in config.sections():
    print(key)
    for k, v in config[key].items():
        print("\t", k, v)




