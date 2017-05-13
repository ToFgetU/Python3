#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Panfei Liu

import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9'
}

config["bitbucket.org"] = {}
config["bitbucket.org"]["User"] = "hr"

config["topsecret.server.com"] = {}
config["topsecret.server.com"]["Host Port"] = "50022"
config["topsecret.server.com"]["ForwardX11"] = "no"

config["DEFAULT"]["ForwardX11"] = "yes"

with open("config.ini", "w") as f:
    config.write(f)