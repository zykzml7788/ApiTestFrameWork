#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:59
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336


# mock项目地址：https://github.com/UncleYong/mock_test

import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import unittest
import requests
from core import HTMLTestRunner
from core import logger
import inspect
from core.tools import p


class SelectMock(unittest.TestCase):
    def setUp(self):
        print('测试用例开始执行...')

    def tearDown(self):
        print('测试用例执行完成...')

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    def test_select_all(self):
        """查询所有"""
        logger.logger.logger.debug('当前方法: %s'%p.get_current_function_name())
        # 优化：ip端口可以放到配置中
        url = 'http://127.0.0.1:5000/api/user'
        try:
            res = requests.get(url=url).json()
        except Exception as e:
            # res = '连接错误。'
            res = {'code':'999','msg':'连接错误。'}
        # print(res,type(res))
        logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))
        
        self.assertEqual(res['code'], '00')

    def test_select_one_exist_first(self):
        """查询一个存在的"""
        url = 'http://127.0.0.1:5000/api/user/1'
        try:
            res = requests.get(url=url).json()
        except Exception as e:
            # res = '连接错误。'
            res = {'code':'999','msg':'连接错误。'}
        # print(res,type(res))
        logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))
        
        self.assertEqual(res['code'], '00')

    def test_select_one_exist_last(self):
        """查询一个存在的"""
        url = 'http://127.0.0.1:5000/api/user/3'
        try:
            res = requests.get(url=url).json()
        except Exception as e:
            # res = '连接错误。'
            res = {'code':'999','msg':'连接错误。'}
        # print(res,type(res))
        logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))
        
        self.assertEqual(res['code'], '00')

    def test_select_one_notExist(self):
        """查询一个不存在的"""
        url = 'http://127.0.0.1:5000/api/user/999'
        try:
            res = requests.get(url=url).json()
        except Exception as e:
            # res = '连接错误。'
            res = {'code':'999','msg':'连接错误。'}
        # print(res,type(res))
        logger.logger.logger.debug('是测试点"%s"下的用例"%s",返回的结果res=%s]'%(self.__class__.__name__, getattr(self, self.get_current_function_name()).__doc__, res))
        
        self.assertEqual(res['code'], '01')


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(SelectMock("test_select_all"))
    suit.addTest(SelectMock("test_select_one_exist_first"))
    suit.addTest(SelectMock("test_select_one_exist_last"))
    suit.addTest(SelectMock("test_select_one_notExist"))
    fp = open("./report.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'**项目接口自动化测试报告',description=u'**项目接口自动化测试报告')
    runner.run(suit)
    fp.close()

# if __name__ == '__main__':
#     unittest.main()