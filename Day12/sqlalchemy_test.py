#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# echo=True  打印详细信息
t_engine = create_engine("mysql+pymysql://root:123456@192.168.128.133:3306/learndb?charset=utf8",
                                    encoding='utf-8', echo=True)
# 生成ORM基类
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users' # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<Users(name='%s', password='%s')>" % (self.name, self.password)

# 创建表结构
Base.metadata.create_all(t_engine)

# 创建数据库的会话 session_class ,注意, 这里返回给session的是class, 不是实例
Session_class = sessionmaker(bind=t_engine)

# 创建实例 同 cursor
session = Session_class()

# 生成你要创建的数据对象
user_obj = Users(name='test', password='123')

# 在这还没有创建数据对象
print('user_obj:', user_obj.name, user_obj.id)

# 把要创建的数据统一加进 session 中， 统一创建
# session.add(user_obj)

# 统一提交, 创建数据
session.commit()

#  数据查询
my_user = session.query(Users).filter_by(name='test').first()
print(my_user)
# print(my_user.id, my_user.name, my_user.password)
