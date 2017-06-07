# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pickle
import time
import os
from conf import settings
from core import identifier

class BaseModel(object):
    '''基类，所有的公共方法都在这里实现'''
    def save(self):
        file_path = os.path.join(self.db_path, str(self.nid))
        pickle.dump(self, open(file_path, 'wb'))

    @classmethod
    def get_all_obj_list(cls):
        '''类方法，获取所有数据'''
        ret = []
        for filename in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path, filename)
            ret.append(pickle.load(open(file_path, 'rb')))
        return ret

class Admin(BaseModel):
    db_path = settings.ADMIN_DB

    def __init__(self, username, password):
        self.nid = identifier.AdminNid(self.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')

    @staticmethod
    def login():
        try:
            user = input("请输入用户名: ").strip()
            passwd = input("请输入密码: ").strip()

            for obj in Admin.get_all_obj_list():
                if obj.username == user and obj.password == passwd:
                    status = True
                    error = ''
                    data = "\033[45;1m登录成功\033[0m"
                    break
            else:
                raise Exception('\033[43;1m用户名或密码错误\033[0m' %name)
        except Exception as e:
            status = False
            error = str(e)
            data = ''
        return {'status': status, 'error': error, 'data': data}


class Classes(BaseModel):
    db_path = settings.CLASSES_DB
    def __init__(self, name, tuition, school_nid, course_to_teacher_list):
        self.nid = identifier.ClassesNid(self.db_path)
        self.name = name
        self.tuition = tuition
        self.school_nid = school_nid
        self.course_to_teacher_list = course_to_teacher_list

class Course(BaseModel):
    db_path = settings.COURSE_DB
    def __init__(self, name, price, period, school_nid):
        self.nid = identifier.CourseNid(self.db_path)
        self.name = name
        self.price = price
        self.period = period
        self.school_nid = school_nid

class Course_to_teacher(BaseModel):
    db_path = settings.COURSE_TO_TEACHER_DB
    def __init__(self, course_nid, school_nid):
        self.nid = identifier.Course_to_teacherNid(self.db_path)
        self.course_nid = course_nid
        self.school_nid = school_nid

class School(BaseModel):
    db_path = settings.SCHOOL_DB
    def __init__(self, name, addr):
        self.nid = identifier.SchoolNid(self.db_path)
        self.name = name
        self.addr = addr
        self.create_time = time.strftime('%Y-%m-%d %X')

class Score:
    def __init__(self, nid):
        self.nid = nid
        self.score_dict = {}

    def set(self, course_to_teacher_nid, number):
        self.score_dict[course_to_teacher_nid] = number

    def get(self, course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid)

class Student(BaseModel):
    db_path = settings.STUDENT_DB
    def __init__(self, name, age, qq, classes_nid):
        self.nid = identifier.StudentNid(self.db_path)
        self.name = name
        self.age = age
        self.qq = qq
        self.classes_nid = classes_nid
        self.score = Score(self.nid)

class Teacher(BaseModel):
    db_path = settings.TEACHER_DB
    def __init__(self, name, level):
        self.nid = identifier.TeacherNid(self.db_path)
        self.name = name
        self.level = level
        self.__account = 0
        self.create_time = time.strftime('%Y-%m-%d %X')