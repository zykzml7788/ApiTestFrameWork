#!/user/bin/env python
#coding=utf-8
'''
@project : my_rf
@author  : djcps
#@file   : test_case.py
#@ide    : PyCharm
#@time   : 2019-05-28 12:37:01
'''
#coding=utf-8

import unittest
from ddt import *
from core.readExcel import *
from core.testBase import *
import jsonpath
from core.functions import *




@ddt
class Test(unittest.TestCase):

    api_data = read_excel()

    #全局变量池
    saves = {}
    #识别${key}的正则表达式
    EXPR = '\$\{(.*?)\}'
    #识别函数助手
    FUNC_EXPR = '__.*?\(.*?\)'

    def save_date(self,source,key,jexpr):
        '''
        提取参数并保存至全局变量池
        :param source: 目标字符串
        :param key: 全局变量池的key
        :param jexpr: jsonpath表达式
        :return:
        '''
        value = jsonpath.jsonpath(source,jexpr)[0]
        self.saves[key] = value
        logger.info("保存 {}=>{} 到全局变量池".format(key,value))

    def build_param(self,string):
        '''
        识别${key}并替换成全局变量池的value,处理__func()函数助手
        :param str: 待替换的字符串
        :return:
        '''

        #遍历所有取值并做替换
        keys = re.findall(self.EXPR, string)
        for key in keys:
            value = self.saves.get(key)
            string = string.replace('${'+key+'}',str(value))


        #遍历所有函数助手并执行，结束后替换
        funcs = re.findall(self.FUNC_EXPR, string)
        for func in funcs:
            fuc = func.split('__')[1]
            fuc_name = fuc.split("(")[0]
            fuc = fuc.replace(fuc_name,fuc_name.lower())
            value = eval(fuc)
            string = string.replace(func,str(value))
        return string

    @classmethod
    def setUpClass(cls):
        # 实例化测试基类，自带cookie保持
        cls.request = BaseTest()


    @classmethod
    def tearDownClass(cls):
        pass

    @data(*api_data)
    @unpack
    def test_(self,descrption,url,method,headers,cookies,params,body,file,verify,saves):
        logger.info("用例描述====>"+descrption)
        url = self.build_param(url)
        headers = self.build_param(headers)
        params = self.build_param(params)
        body = self.build_param(body)
        res = None
        params = eval(params) if params else params
        headers = eval(headers) if headers else headers
        cookies = eval(cookies) if cookies else cookies
        body = eval(body) if body else body
        file = eval(file) if file else file
        if method.upper() == 'GET':
            res = self.request.get_request(url=url,params=params,headers=headers,cookies=cookies)
        elif method.upper() == 'POST':
            res = self.request.post_request(url=url,headers=headers,cookies=cookies,params=params,json=body)
        if method.upper() == 'UPLOAD':
            res = self.request.upload_request(url=url,headers=headers,cookies=cookies,params=params,data=body,files=file)
        else:
            #待扩充，如PUT,DELETE方法
            pass
        if saves:
            # 遍历saves
            for save in saves.split(";"):
                # 切割字符串 如 key=$.data
                key = save.split("=")[0]
                jsp = save.split("=")[1]
                self.save_date(res.json(), key, jsp)
        if verify:
            # 遍历verify:
            for ver in verify.split(";"):
                expr = ver.split("=")[0]
                # 判断Jsonpath还是正则断言
                if expr.startswith("$."):
                    actual = jsonpath.jsonpath(res.json(), expr)[0]
                else:
                    actual = re.findall(expr,res.text)[0]
                expect = ver.split("=")[1]
                self.request.assertEquals(actual, expect)


