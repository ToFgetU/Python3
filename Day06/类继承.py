#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

class Person(object):
    def __init__(self, name, age, sex):
        self.NAME = name
        self.AGE = age
        self.SEX = sex

    def talk(self):
        print("is talking ...")

class BlackPerson(Person):
    def __init__(self, name, age, sex, strength):
        Person.__init__(self, name, age, sex)
        self.strength = strength
        print(self.NAME, self.AGE, self.SEX)

    def talk(self):
        print("%s is talking ..." % self.NAME)

b = BlackPerson('test', 22, '11', 'strong')
b.talk()