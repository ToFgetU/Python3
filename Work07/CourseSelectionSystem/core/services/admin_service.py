#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

from core.models import Admin
from core.models import Teacher
from core.models import Course
from core.models import School
from core.models import Student
from core.models import Course_to_teacher
from core.models import Classes

def create_school():
    try:
        print('创建学校'.center(60, '='))
        name = input("请输入学校名字: ").strip()
        addr = input("请输入学校地址: ").strip()
        if name == '' or addr == '':
            raise Exception("输入不能为空")
        school_name_list = [(obj.name, obj.addr) for obj in School.get_all_obj_list()]
        if (name, addr) in school_name_list:
            raise Exception('\033[43;1m[%s] [%s]校区 已经存在,不可重复创建\033[0m' % (name, addr))
        obj = School(name, addr)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m[%s] [%s]校区 创建成功\033[0m' %(obj.name,obj.addr)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_school():
    for obj in School.get_all_obj_list():
        print('\033[45;1m学校[%s] 地址[%s] 创建日期[%s]\033[0m'.center(60, '-') \
              % (obj.name, obj.addr, obj.create_time))

def create_teacher():
    try:
        print('创建老师'.center(60, '='))
        name = input("请输入老师姓名: ").strip()
        level = input("请输入老师级别").strip()
        if name == '' or level == '':
            raise Exception("输入不能为空")

        teacher_name_list = [obj.name for obj in Teacher.get_all_obj_list()]
        if name in teacher_name_list:
            raise Exception('\033[43;1m老师[%s] 已经存在,不可重复创建\033[0m' % (name))
        obj = Teacher(name, level)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m老师[%s] 级别[%s] 时间[%s]创建成功\033[0m' %(obj.name,obj.level,obj.create_time)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_teacher():
    for obj in Teacher.get_all_obj_list():
        print('\033[33;1m老师[%s] 级别[%s] 创建时间[%s]\033[0m'.center(60, '-') \
              % (obj.name, obj.level, obj.create_time))

def create_course():
    try:
        print('创建课程'.center(60, '='))
        school_list = School.get_all_obj_list()
        for k, obj in enumerate(school_list):
            print(k, obj.name, obj.addr)
        sid = input("请选择学校: ").strip()
        if sid.isdigit():
            sid = int(sid)
            if sid >= len(school_list):
                raise  Exception("输入的学校不存在")
        else:
            raise Exception("输入的学校不存在")

        school_obj = school_list[sid]
        name = input("请输入课程名称: ").strip()
        price = input("请输入课程费用: ").strip()
        if name == '' or price == '':
            raise Exception("输入不能为空")
        if price.replace('.', '', 1).isdigit():
            pass
        else:
            raise Exception("课程费用应该是数字")
        period = input("请输入课程周期: ").strip()
        if period == '':
            raise Exception("输入不能为空")

        course_name_list = [(obj.name, obj.school_nid.nid) for obj in Course.get_all_obj_list()]
        if (name, school_obj.nid.nid) in course_name_list:
            raise Exception('\033[43;1m课程[%s] 已经存在,不可重复创建\033[0m' % (name))
        obj = Course(name, price, period, school_obj.nid)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m课程[%s] 价格[%s] 周期[%s]创建成功\033[0m' % (obj.name, obj.price, obj.period)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_course():
    for obj in Course.get_all_obj_list():
        print('\033[33;1m[%s] [%s]校区 [%s]课程 价格[%s] 周期[%s]\033[0m'.center(60, '-') \
              % (obj.school_nid.get_obj_by_nid().name, obj.school_nid.get_obj_by_nid().addr, \
                 obj.name, obj.price, obj.period))

def create_course_to_teacher():
    try:
        teacher_list = Teacher.get_all_obj_list()
        for k, obj in enumerate(teacher_list):
            print(k, obj.name)
        t_sid = input("请选择老师:")
        if t_sid.isdigit():
            t_sid = int(t_sid)
            if t_sid >= len(teacher_list):
                raise  Exception("选择的老师不在此任教")
        else:
            raise Exception("选择的老师不在此任教")
        teacher_obj = teacher_list[t_sid]


        course_list = Course.get_all_obj_list()
        for k, obj in enumerate(course_list):
            print(k, obj.name)
        c_sid = input("\n请选择关联课程: ")
        if c_sid.isdigit():
            c_sid = int(c_sid)
            if c_sid >= len(course_list):
                raise Exception("没有该课程")
        else:
            raise Exception("没有该课程")
        course_obj = course_list[c_sid]

        course_to_teacher_list = [(obj.course_nid, obj.school_nid, obj.teacher_nid) for obj in Course_to_teacher.get_all_obj_list()]
        if (course_obj.nid, course_obj.school_nid, teacher_obj.nid) in course_to_teacher_list:
            raise Exception('\033[43;1m课程[%s] 与老师[%s],不可重复关联\033[0m' % (course_obj.name, teacher_obj.name))
        obj = Course_to_teacher(course_obj.nid, course_obj.school_nid, teacher_obj.nid)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m课程[%s] 与老师[%s]关联成功\033[0m' % ((course_obj.name, course_obj.school_nid.get_obj_by_nid().name), teacher_obj.name)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}


def create_classes():
    try:
        print('创建班级'.center(60, '='))
        school_list = School.get_all_obj_list()
        for k, obj in enumerate(school_list):
            print(k, obj.name, obj.addr)
        sid = input("请选择学校:")
        if sid.isdigit():
            sid = int(sid)
            if sid >= len(school_list):
                raise  Exception("输入的学校不存在")
        else:
            raise Exception("输入的学校不存在")
        school_obj = school_list[sid]
        name = input("请输入班级名称: ")
        course_to_teacher_list = Course_to_teacher.get_all_obj_list()
        for k, obj in enumerate(course_to_teacher_list):
            if school_obj.nid.nid == course_to_teacher_list[k].school_nid.nid:
                print(k, '课程[%s] 讲师[%s] [%s] [%s]校区' % (obj.course_nid.get_obj_by_nid().name, obj.teacher_nid.get_obj_by_nid().name,
                      obj.school_nid.get_obj_by_nid().name, obj.school_nid.get_obj_by_nid().addr))

        choice = input("请选择关联课程:")
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(course_to_teacher_list):
                raise Exception("没有该课程")
        else:
            raise Exception("没有该课程")
        obj = Classes(name, school_obj.nid, course_to_teacher_list[choice].nid)
        obj.save()
        status = 'True'
        error =''
        data = '\033[33;1m班级[%s]创建成功\033[0m' % (name)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_classes():
    for obj in Classes.get_all_obj_list():
        print('\033[33;1m [%s][%s]校区  班级[%s] \033[0m'.center(60, '-') \
              % (obj.school_nid.get_obj_by_nid().name, obj.school_nid.get_obj_by_nid().addr, obj.nid.get_obj_by_nid().name))

def create_student():
    try:
        print('创建学生'.center(60, '='))
        name = input("请输入姓名: ").strip()
        age = input("请输入年龄: ").strip()
        if name == '' or age == '':
            raise Exception("输入不能为空")
        if age.isdigit():
            age = int(age)
        else:
            raise Exception("年龄应该是数字")
        student_name_list = [obj.name for obj in Student.get_all_obj_list()]
        if name in student_name_list:
            raise Exception("学生[%s]已存在" % name)

        school_list = School.get_all_obj_list()
        for k, obj in enumerate(school_list):
            print(k, '[%s] [%s]校区' % (obj.name, obj.addr))
        s_sid = input("请选择学校:")
        if s_sid.isdigit():
            s_sid = int(s_sid)
            if s_sid >= len(school_list):
                raise Exception("输入的学校不存在")
        else:
            raise Exception("输入的学校不存在")

        classes_list = Classes.get_all_obj_list()
        for k, obj in enumerate(classes_list):
            print(k, obj.name, '[%s]校区' % (obj.school_nid.get_obj_by_nid().addr))
        sid = input("请选择班级:")
        if sid.isdigit():
            sid = int(sid)
            if sid >= len(classes_list):
                raise Exception("输入的班级不存在")
        else:
            raise Exception("输入的班级不存在")
        if school_list[s_sid].nid.nid != classes_list[sid].school_nid.nid:
            raise Exception("[%s][%s]校区没有 [%s]班级" % (school_list[s_sid].name, school_list[s_sid].addr, classes_list[sid].name))

        print("学费为: ", classes_list[sid].course_to_teacher_list_nid.get_obj_by_nid().course_nid.get_obj_by_nid().price)
        obj = Student(name, age, classes_list[sid].nid)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m学生[%s] 创建成功\033[0m' % name
    except Exception as e:
        status = False
        error = str(e)
        data = ''

    return {'status': status, 'error': error, 'data': data}


def show_student():
    for obj in Student.get_all_obj_list():
        print('\033[33;1m [%s][%s]校区  班级[%s] 学生[%s] \033[0m'.center(60, '-') \
              % (obj.classes_nid.get_obj_by_nid().school_nid.get_obj_by_nid().name,
                 obj.classes_nid.get_obj_by_nid().school_nid.get_obj_by_nid().addr,
                 obj.classes_nid.get_obj_by_nid().name, obj.name))

def show():
    msg = '''
    0:选项
    1:创建学校
    2:查看学校
    3:创建老师
    4:查看老师
    5:创建课程
    6:查看课程
    7:关联老师与课程
    8:创建班级
    9:查看班级
    10:创建学生
    11:查看学生
    12:退出
    '''
    print(msg)

def main():
    choice_dict = {
        '0': show,
        '1': create_school,
        '2': show_school,
        '3': create_teacher,
        '4': show_teacher,
        '5': create_course,
        '6': show_course,
        '7': create_course_to_teacher,
        '8': create_classes,
        '9': show_classes,
        '10': create_student,
        '11': show_student,
        '12': exit
    }
    show()
    while True:
        choice = input("请输入选项 : ").strip()
        if choice not in choice_dict:
            print("输入的选项不存在")
            continue
        ret = choice_dict[choice]()
        if ret:
            if ret['status']:
                print(ret['data'].center(60, '-'))
            else:
                print(ret['error'].center(60, '-'))

def login():
    ret = Admin.login()
    if ret:
        if ret['status']:
            print(ret['data'].center(60, '-'))
            main()
        else:
            print(ret['error'].center(60, '-'))