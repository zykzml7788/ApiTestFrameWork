#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:59
# @Author  : wengy
# @Email   : 1915992513@qq.com
# @Blog    : http://www.cnblogs.com/UncleYong
# @GitHub  : https://github.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong

import os
import sys


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)
sys.path.insert(0, path)
from conf.settings import TESTCASE_PATH
from conf.settings import REPORT_PATH
import unittest
from core import HTMLTestRunner
import time

suit = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    fp = open(REPORT_PATH + now + "_report.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'**项目测试报告',
        description=u'测试报告可通过本机访问测试服务器查看，地址：http://<测试服务器IP>:8000/')
    runner.run(suit)
    fp.close()
