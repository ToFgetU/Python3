#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os,sys
DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
from core import main
if __name__ == '__main__':
    server = main.MyParser()