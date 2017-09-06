#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

t_engine = create_engine("mysql+pymysql://root:123456@192.168.128.133:3306/learndb",
                                    encoding='utf-8', echo=True)
# 生成ORM基类
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users' # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

# 创建表结构
Base.metadata.create_all(t_engine)