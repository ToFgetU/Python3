#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
from core.models import Admin
from conf import settings

def initialize():
    try:
        username = input("请输入管理员账户名: ").strip()
        password = input("请输入初始化密码: ").strip()
        obj = Admin(username, password)
        obj.save()
        return True
    except Exception as e:
        print(e)

def clean_all():
    try:
        choice = input("是否初始化程序(y/n): ").strip()
        if choice.lower() == 'y':
            db_path = [settings.ADMIN_DB, settings.CLASSES_DB, settings.COURSE_DB, settings.COURSE_TO_TEACHER_DB,
                       settings.SCHOOL_DB, settings.STUDENT_DB, settings.TEACHER_DB, settings.TEACHING_DB]
            for i in db_path:
                for f in os.listdir(i):
                    f = os.path.join(i, f)
                    # print(f)
                    os.remove(f)
        else:
            pass
        return True
    except Exception as e:
        print(e)

def main():
    show = """
        1. 初始化管理员账户
        2. 初始化程序
    """

    choice_dict = {
        '1': initialize,
        '2': clean_all
    }
    while True:
        print(show)
        choice = input("请输入操作选项: ").strip()
        print(choice)
        if choice not in choice_dict:
            print('选项错误，请重新输入！！！')
            continue
        func = choice_dict[choice]
        ret = func()
        if ret:
            print('操作成功')
            return
        else:
            print('操作异常，请重新操作')
