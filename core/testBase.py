#!/user/bin/env python
#coding=utf-8
'''
@project : bitest
@author  : djcps
#@file   : testBase.py
#@ide    : PyCharm
#@time   : 2019-05-05 10:23:02
'''
import requests
from json import dumps
from core.logger import Logger
from requests.packages.urllib3.exceptions import InsecureRequestWarning

logger = Logger().logger

# 禁用安全请求警告



requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class BaseTest(requests.Session):

    '''
        接口基类，供后续脚本使用
    '''



    def get_request(self,url,headers=None,params=None,cookies=None):
        '''
        get请求方法
        :param url: 地址
        :param headers: 请求头
        :param params: 请求参数
        :param cookies:
        :return:
        '''
        try:
            res = self.request('GET',url,headers=headers,params=params,cookies=cookies,verify=False)
            self.api_log('GET',url,headers=headers,params=params,cookies=cookies,
                     code=res.status_code,res_text=res.text,res_header=res.headers)
            return res
        except Exception as e:
            logger.error("接口请求异常,原因：{}".format(e))
            raise e

    def post_request(self,url,headers=None,data=None,json=None,params=None,cookies=None):
        '''
        post请求方法
        :param url: 接口地址
        :param headers: 请求头
        :param json: 请求体
        :param params: 请求参数
        :param cookies:
        :return:
        '''
        try:
            res = self.request('POST', url, headers=headers, params=params,data=data,
                               json=json,cookies=cookies,verify=False)
            self.api_log('POST', url, headers=headers, params=params,json=json, cookies=cookies,
                         code=res.status_code, res_text=res.text,res_header=res.headers)
            return res

        except Exception as e:
            logger.error("接口请求异常,原因：{}".format(e))
            raise e

    def upload_request(self,url,headers=None,data=None,files=None,json=None,params=None,cookies=None):
        try:

            filename = list(files.keys())[0]
            filepath = list(files.values())[0]
            with open(filepath,'rb') as file:
                files["{}".format(filename)] = file
                res = self.request('POST', url, headers=headers, params=params,data=data,
                               files=files,json=json,cookies=cookies,verify=False)
            self.api_log('UPLOAD', url, headers=headers, params=params,json=data,file=filepath, cookies=cookies,
                         code=res.status_code, res_text=res.text,res_header=res.headers)
            return res

        except Exception as e:
            logger.error("接口请求异常,原因：{}".format(e))
            raise e

    def assertEquals(self,actual,expected):
        '''
        断言是否等于
        :param actual: 实际值
        :param expected: 预期值
        :return:
        '''
        try:
            assert actual == expected
            logger.info("断言成功,实际值：{} 等于 预期值：{}".format(actual, expected))
        except AssertionError as e:
            logger.error("断言失败,实际值：{} 不等于 预期值：{}".format(actual,expected))
            raise AssertionError

    def assertTrue(self,actual):
        '''
        断言是否为真
        :param actual: 实际值
        :return:
        '''
        try:
            assert actual == True
            logger.info("断言成功,实际值：{} 为真".format(actual))
        except AssertionError as e:
            logger.error("断言失败,实际值：{} 不为真".format(actual))
            raise AssertionError

    def assertIn(self,content,target):
        '''
        断言是否包含
        :param content: 包含文本
        :param target: 目标文本
        :return:
        '''
        try:
            assert content in target
            logger.info("断言成功,目标文本：{} 包含 文本：{}".format(target,content))
        except AssertionError as e:
            logger.error("断言失败,目标文本：{} 不包含 文本：{}".format(target,content))
            raise AssertionError


    def api_log(self,method,url,headers=None,params=None,json=None,cookies=None,file=None,code=None,res_text=None,res_header=None):
        logger.info("请求方式====>{}".format(method))
        logger.info("请求地址====>{}".format(url))
        logger.info("请求头====>{}".format(dumps(headers,indent=4)))
        logger.info("请求参数====>{}".format(dumps(params,indent=4)))
        logger.info("请求体====>{}".format(dumps(json,indent=4)))
        logger.info("上传附件为======>{}".format(file))
        logger.info("Cookies====>{}".format(dumps(cookies,indent=4)))
        logger.info("接口响应状态码====>{}".format(code))
        logger.info("接口响应头为====>{}".format(res_header))
        logger.info("接口响应体为====>{}".format(res_text))



