#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:59
# @Author  : wengy
# @Email   : 1915992513@qq.com
# @Blog    : http://www.cnblogs.com/UncleYong
# @GitHub  : https://github.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong

import redis
import json

r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='uncleyong@uncleyong')
r.set('verification_code:register13811228811','{"validateCode":"111111","time":"1526523665998"}')
# res = json.loads(r.get('verification_code:register13811228811').decode('utf-8'))
# print(res,type(res))
# print(res['validateCode'])