#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:59
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336

import os
import sys

# 获取项目的目录
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)

# 把path加入环境变量，0表示放在最前面，因为python解释器会按照列表顺序去依次到每个目录下去匹配你要导入的模块名，
# 只要在一个目录下匹配到了该模块名，就立刻导入，不再继续往后找
sys.path.insert(0, path)
# 导入配置文件中定义的测试用例的路径
from conf.settings import TESTCASE_PATH
# 导入配置文件中定义的测试报告的路径
from conf.settings import REPORT_PATH
import unittest
# 导入报告模板
from core import HTMLTestRunner
import time
# 自动根据测试用例的路径匹配查找测试用例文件（*.py）,并将查找到的测试用例组装到测试套件中
suit = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='test_*.py')

if __name__ == '__main__':
	# 获取当前时间并指定时间格式
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 创建报告文件
    fp = open(REPORT_PATH + now + "_report.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'**项目接口自动化测试报告',
        description=u'测试报告也可访问测试服务器查看，地址：http://<测试服务器IP>:8000/')
    runner.run(suit)
    fp.close()
