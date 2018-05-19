#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:59
# @Author  : wengy
# @Email   : 1915992513@qq.com
# @Blog    : http://www.cnblogs.com/UncleYong
# @GitHub  : https://github.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong

import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTCASE_PATH =  os.path.join(BASE_PATH,'test_case')
REPORT_PATH =  os.path.join(BASE_PATH,'report/')
LOG_PATH = os.path.join(BASE_PATH,'log/log.txt')

DB_NAME = 'uncleyong'
DB_PASSWORD = '123456'
DB_IP = '127.0.0.1'
DB = 'oracledb'

# print(BASE_PATH)
# print(TESTCASE_PATH)
# print(REPORT_PATH)
# print(LOG_PATH)


