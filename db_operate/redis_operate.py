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
import redis
import json
from conf.settings import REDIS_HOST
from conf.settings import REDIS_PORT
from conf.settings import REDIS_DB
from conf.settings import REDIS_PASSWORD


# r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='uncleyong@redis123123')
r = redis.Redis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DB,password=REDIS_PASSWORD)
# 往redis中加一个短信验证码，模拟手机发送短信的功能
r.set('verification_code:register13811228811','{"validateCode":"111111","time":"1526523665998"}')
# res = json.loads(r.get('verification_code:register13811228811').decode('utf-8'))
# print(res,type(res))
# print(res['validateCode'])