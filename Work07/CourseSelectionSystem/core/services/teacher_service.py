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

def show_classes(user):
    '''查看老师所管理的班级'''
    for obj in Classes.get_all_obj_list():
        if user == obj.course_to_teacher_list_nid.get_obj_by_nid().teacher_nid.get_obj_by_nid().name:
            print('\033[33;1m [%s][%s]校区  班级[%s] \033[0m'.center(60, '-') \
                  % (obj.school_nid.get_obj_by_nid().name, obj.school_nid.get_obj_by_nid().addr, obj.nid.get_obj_by_nid().name))

def choice_classes(user):
    '''选择班级进行授课'''
    try:
        choice_list = []
        classes_list = Classes.get_all_obj_list()
        for k, obj in enumerate(classes_list):
            if user == obj.course_to_teacher_list_nid.get_obj_by_nid().teacher_nid.get_obj_by_nid().name:
                print(k, '\033[33;1m [%s][%s]校区  班级[%s] [%s]期 \033[0m' \
                      % (obj.school_nid.get_obj_by_nid().name, obj.school_nid.get_obj_by_nid().addr,
                         obj.nid.get_obj_by_nid().name, obj.course_to_teacher_list_nid.get_obj_by_nid().course_nid.get_obj_by_nid().period))
                choice_list.append(classes_list[k])
        choice = input("请选择授课班级: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(choice_list):
                raise Exception("班级选择错误")
        else:
            raise Exception("班级选择错误")

        obj = Teaching(obj.course_to_teacher_list_nid.get_obj_by_nid().teacher_nid, choice_list[choice].nid)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m老师[%s]在[%s]创建了一条上课记录\033[0m' % (user, obj.create_time)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_student(user):
    try:
        choice_list = []
        classes_list = Classes.get_all_obj_list()
        student_list = Student.get_all_obj_list()
        for k, obj in enumerate(classes_list):
            if user == obj.course_to_teacher_list_nid.get_obj_by_nid().teacher_nid.get_obj_by_nid().name:
                print(k, '\033[33;1m [%s][%s]校区  班级[%s] [%s]期 \033[0m' \
                      % (obj.school_nid.get_obj_by_nid().name, obj.school_nid.get_obj_by_nid().addr,
                         obj.nid.get_obj_by_nid().name,
                         obj.course_to_teacher_list_nid.get_obj_by_nid().course_nid.get_obj_by_nid().period))
                choice_list.append(classes_list[k])
        choice = input("请选择查看的班级: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(choice_list):
                raise Exception("班级选择错误")
        else:
            raise Exception("班级选择错误")
        for k, obj in enumerate(student_list):
            if choice_list[choice].nid.nid == student_list[k].classes_nid.nid:
                print('\033[33;1m班级[%s] [%s]期 学员[%s] 成绩[%s]\033[0m' % (obj.classes_nid.get_obj_by_nid().name,
                       obj.classes_nid.get_obj_by_nid().course_to_teacher_list_nid.get_obj_by_nid().course_nid.get_obj_by_nid().period,
                       obj.name, obj.score.get(obj.classes_nid.get_obj_by_nid().course_to_teacher_list_nid.nid)))
    except Exception as e:
        status = False
        error = str(e)
        data = ''
        return {'status': status, 'error': error, 'data': data}

def change_score(user):
    try:
        choice_list = []
        classes_list = Classes.get_all_obj_list()
        student_list = Student.get_all_obj_list()
        for k, obj in enumerate(classes_list):
            if user == obj.course_to_teacher_list_nid.get_obj_by_nid().teacher_nid.get_obj_by_nid().name:
                print(k, '\033[33;1m [%s][%s]校区  班级[%s] [%s]期 \033[0m' \
                      % (obj.school_nid.get_obj_by_nid().name, obj.school_nid.get_obj_by_nid().addr,
                         obj.nid.get_obj_by_nid().name,
                         obj.course_to_teacher_list_nid.get_obj_by_nid().course_nid.get_obj_by_nid().period))
                choice_list.append(classes_list[k])
        choice = input("请选择查看的班级: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(choice_list):
                raise Exception("班级选择错误")
        else:
            raise Exception("班级选择错误")
        tmp = []
        for k, obj in enumerate(student_list):
            if choice_list[choice].nid.nid == student_list[k].classes_nid.nid:
                tmp.append(k)
                print(k, '\033[33;1m班级[%s] [%s]期 学员[%s] 成绩[%s]\033[0m' % (obj.classes_nid.get_obj_by_nid().name,
                            obj.classes_nid.get_obj_by_nid().course_to_teacher_list_nid.get_obj_by_nid().course_nid.get_obj_by_nid().period,
                            obj.name, obj.score.get(obj.classes_nid.get_obj_by_nid().course_to_teacher_list_nid.nid)))
        change = input("选择要修改的学生:")
        if change.isdigit():
            change = int(change)
            if change in tmp:
                num = input("请输入该学生的成绩:")
                file_path = os.path.join(settings.STUDENT_DB, student_list[change].nid.nid)
                student_list[change].score.set(obj.classes_nid.get_obj_by_nid().course_to_teacher_list_nid.nid, num)
                obj = student_list[change]
                pickle.dump(obj, open(file_path, 'wb'))
                print(obj.score.get(obj.classes_nid.get_obj_by_nid().course_to_teacher_list_nid.nid))
                status = True
                error = ''
                data = '\033[33;1m学生[%s] 成绩为[%s]\033[0m' % (student_list[change].name, num)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_teaching(user):
    for obj in  Teaching.get_all_obj_list():
        if user == obj.teacher_nid.get_obj_by_nid().name:
            print('\033[33;1m老师[%s]在[%s]给[%s]班级上了一堂课\033[0m' % (obj.teacher_nid.get_obj_by_nid().name,
                        obj.create_time, obj.classes_nid.get_obj_by_nid().name))

def show():
    msg = '''
    0:选项
    1:查看管理班级
    2:授课管理班级
    3:查看管理学生
    4:修改学生成绩
    5:查看授课记录
    6:退出
    '''
    print(msg)

def main(user):
    choice_dict = {
        '0': show,
        '1': show_classes,
        '2': choice_classes,
        '3': show_student,
        '4': change_score,
        '5': show_teaching,
        '6': exit
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
    ret = Teacher.login()
    if ret:
        if ret['status']:
            print(ret['data'].center(60, '-'))
            main(ret['user'])
        else:
            print(ret['error'].center(60, '-'))