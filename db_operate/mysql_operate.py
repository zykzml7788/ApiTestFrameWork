#!/user/bin/env python
#coding=utf-8
'''
@project : ApiTestFrameWork
@author  : djcps
#@file   : mysql_operate.py
#@ide    : PyCharm
#@time   : 2019-06-18 18:43:48
'''
from conf.settings import *
import pymysql

class MySQLOperate():
    '''
        mysql执行器
    '''
    def __init__(self,DB):

        self.db = pymysql.Connect(
            host=DB_IP,
            user=DB_NAME,
            password=DB_PASSWORD,
            database=DB,
            port=PORT
        )

    def execute_sql(self,sql):
        '''
        执行sql
        :param sql: 增删改查
        :return:
        '''
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        result = cursor.execute(sql)
        if sql.lower().startswith("select"):
            return cursor.fetchone()
        else:
            self.db.commit()
            return result
        # return cursor.fetchone()


if __name__ == '__main__':
    print(MySQLOperate("test").execute_sql("select *from student" ))