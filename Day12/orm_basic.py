#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 建立数据库连接
engine = create_engine("mysql+pymysql://root:mysql@192.168.128.133:3306/learndb", encoding='utf-8', echo=True)
# engine = create_engine("oracle+cx_oracle://dev:dev@192.168.128.131:1521/orcl", encoding='utf-8', echo=True)
# 建立orm基类
Base = declarative_base()
#建表
class User(Base):
    __tablename__ = 'user' # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

# 创建表结构
Base.metadata.create_all(engine)
# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
# 生成session实例
session = Session_class()

# 生成要创建的数据对象
user_obj = User(name='alex', password='123')
# 此时还没创建对象呢，不信你打印一下id发现还是None
print(user_obj.name, user_obj.id)
# 把要创建的数据对象添加到这个session里， 一会统一创建
session.add(user_obj)
print(user_obj.name, user_obj.id) # 此时也依然还没创建
session.commit() # 现此才统一提交，创建数据
