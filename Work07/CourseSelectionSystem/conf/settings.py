#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB = os.path.join(BASE_DIR, 'db', 'admin')
CLASSES_DB = os.path.join(BASE_DIR, 'db', 'classes')
COURSE_DB = os.path.join(BASE_DIR, 'db', 'course')
COURSE_TO_TEACHER_DB = os.path.join(BASE_DIR, 'db', 'course_to_teacher')
SCHOOL_DB = os.path.join(BASE_DIR, 'db', 'school')
STUDENT_DB = os.path.join(BASE_DIR, 'db', 'student')
TEACHER_DB = os.path.join(BASE_DIR, 'db', 'teacher')
TEACHING_DB = os.path.join(BASE_DIR, 'db', 'givelessons')