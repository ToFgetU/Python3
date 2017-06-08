#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pickle
import os
from core.models import Teacher
from core.models import Course
from core.models import School
from core.models import Student
from core.models import Course_to_teacher
from core.models import Classes
from core.models import Teaching
from conf import settings
from core.services import admin_service

def show_classes(user):
    for obj in Classes.get_all_obj_list():
        print('\033[33;1m [%s][%s]校区  班级[%s] \033[0m'.center(60, '-') \
              % (obj.school_nid.get_obj_by_nid().name, obj.school_nid.get_obj_by_nid().addr, obj.nid.get_obj_by_nid().name))

def show_students(user):
    for obj in Student.get_all_obj_list():
        print('\033[33;1m班级[%s] [%s]期 学员[%s] 成绩[%s]\033[0m' % (obj.classes_nid.get_obj_by_nid().name,
               obj.classes_nid.get_obj_by_nid().course_to_teacher_list_nid.get_obj_by_nid().course_nid.get_obj_by_nid().period,
               obj.name, obj.score.get(obj.classes_nid.get_obj_by_nid().course_to_teacher_list_nid.nid)))


def show():
    msg = '''
    0:选项
    1:查看班级
    2:查看同学
    3:退出
    '''
    print(msg)

def main(user):
    choice_dict = {
        '0': show,
        '1': show_classes,
        '2': show_students,
        '3': exit
    }
    show()
    while True:
        choice = input("请输入选项 : ").strip()
        if choice not in choice_dict:
            print("输入的选项不存在")
            continue
        ret = choice_dict[choice](user)
        if ret:
            if ret['status']:
                print(ret['data'].center(60, '-'))
            else:
                print(ret['error'].center(60, '-'))

def login():
    msg = '''
    1.注册
    2.登入
    '''
    while True:
        print(msg)
        choice = input("请选择操作: ").strip()
        if choice == '1':
            ret = admin_service.create_student()
        elif choice == '2':
            ret = Student.login()
        else:
            print("输入有误")
            continue

        if ret:
            if ret['status']:
                print(ret['data'].center(60, '-'))
                if choice == '2':
                    main(ret['user'])
            else:
                print(ret['error'].center(60, '-'))