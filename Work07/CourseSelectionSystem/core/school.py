#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

class Person(object):
    def __init__(self, name):
        self.__NAME = name

    def get_name(self):
        return self.__NAME

class Teacher(Person):
    def __init__(self, name):
        super(Teacher, self).__init__(name)

    def talk(self):
        print("%s is talking ..." % self.get_name())

t = Teacher('test')
t.talk()