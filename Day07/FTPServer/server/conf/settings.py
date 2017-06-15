#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_HOME = '%s/home' % BASE_DIR
LOG_DIR = '%s/log' % BASE_DIR
LOG_LEVEL = 'DEBUG'

ACCOUNT_DIR = '%s/db' % BASE_DIR

HOST = 'localhost'
PORT = 10021
