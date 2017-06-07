#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
import pickle
from conf import settings
from lib import commons

class Nid(object):
    '''标记类'''
    def __init__(self, role, db_path):
        role_list = ['admin', 'teacher', 'school', 'course', 'classes', 'student', 'course_to_teacher']
        if role not in role_list:
            raise Exception("用户角色错误，选项: %s" % ','.join(role_list))
        self.role = role
        self.db_path = db_path
        self.nid = commons.create_uuid()

    def __str__(self):
        return self.nid

    def get_obj_by_nid(self):
        '''获取对象标识符'''
        for filename in os.listdir(self.db_path):
            if filename == self.nid:
                return pickle.load(open(os.path.join(self.db_path, filename), 'rb'))
        return None

class AdminNid(Nid):
    def __init__(self, db_path):
        super(AdminNid, self).__init__('admin', db_path)

class ClassesNid(Nid):
    def __init__(self, db_path):
        super(ClassesNid, self).__init__('classes', db_path)

class CourseNid(Nid):
    def __init__(self, db_path):
        super(CourseNid, self).__init__('course', db_path)

class Course_to_teacherNid(Nid):
    def __init__(self, db_path):
        super(Course_to_teacherNid, self).__init__('course_to_teacher', db_path)

class SchoolNid(Nid):
    def __init__(self, db_path):
        super(SchoolNid, self).__init__('school', db_path)

class StudentNid(Nid):
    def __init__(self, db_path):
        super(StudentNid, self).__init__('student', db_path)

class TeacherNid(Nid):
    def __init__(self, db_path):
        super(TeacherNid, self).__init__('teacher', db_path)