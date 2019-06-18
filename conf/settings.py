#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义测试用例的路径
TESTCASE_PATH =  os.path.join(BASE_PATH,'test_case')
# 定义测报告的路径
REPORT_PATH =  os.path.join(BASE_PATH,'report/')
# 定义日志文件的路径
LOG_PATH = os.path.join(BASE_PATH,'log/log.txt')

# mysql数据库的连接信息
DB_NAME = 'root'
DB_PASSWORD = '123456'
DB_IP = '127.0.0.1'
PORT = 3306

# redis数据库的连接信息
# r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='uncleyong@redis123123')
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = ''

# print(BASE_PATH)
# print(TESTCASE_PATH)
# print(REPORT_PATH)
# print(LOG_PATH)


