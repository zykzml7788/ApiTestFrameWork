#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:59
# @Author  : uncleyong
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 66719336

import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)
sys.path.insert(0, path)
import logging
from logging import handlers
from conf.settings import LOG_PATH

class Logger(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance: 
            cls.__instance = object.__new__(cls, *args) 
        return cls.__instance 

    def __init__(self):
        self.formater = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(pathname)s : %(funcName)s:%(lineno)d , %(message)s')
        self.logger = logging.getLogger('log')
        self.logger.setLevel(logging.DEBUG)
        self.filelogger = handlers.RotatingFileHandler(LOG_PATH,
                                                       maxBytes=5242880,
                                                       backupCount=3
                                                       )
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger()

if __name__ == '__main__':
    logger.logger.debug('http://www.cnblogs.com/UncleYong/')

