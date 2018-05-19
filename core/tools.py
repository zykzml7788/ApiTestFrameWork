#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:59
# @Author  : wengy
# @Email   : 1915992513@qq.com
# @Blog    : http://www.cnblogs.com/UncleYong
# @GitHub  : https://github.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong


import sys
import inspect

class GetCurrentItems(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance 
    def __init__(self):
        pass

    @staticmethod
    def get_current_file_path():
        return __file__

    def get_current_class_name(self):
        return self.__class__.__name__

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    @staticmethod
    def get_current_lineno():
        return sys._getframe().f_lineno



p = GetCurrentItems()    
# p2 = GetCurrentItems()   
# p3 = GetCurrentItems() 
# print(p,p2,p3)         

    




