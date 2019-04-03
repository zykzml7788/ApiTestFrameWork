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
import cx_Oracle
from conf.settings import DB_NAME
from conf.settings import DB_PASSWORD
from conf.settings import DB_IP
from conf.settings import DB


class DbOperate(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance: 
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, sql):
        self.name = DB_NAME
        self.password = DB_PASSWORD
        self.ip = DB_IP
        self.db = DB
        self.sql = sql.strip().lower()
	
    def db_operate(self):
        try:
            self.conn = cx_Oracle.connect('%s/%s@%s/%s'%(self.name,self.password,self.ip,self.db))
        except Exception as e:
            return {'code':'12306', 'msg':'数据库连接异常>>>%s'%e}

        self.cur = self.conn.cursor()

        try:
            self.cur.execute(self.sql)
        except Exception as e:
            return {'code':'12307', 'msg':'sql错误>>>%s'%e}
        else:
            if self.sql.startswith('select'):
                ret = self.cur.fetchone()
            else:
                if self.sql.startswith('delete') and self.sql.count('=') != 1:
                    return {'code':'12308', 'msg':'delete操作必须带where条件，一次只能删除一条数据'}
                elif self.sql.startswith('update') and self.sql.count('=') != 2: # 耗时43s
                #elif sql.startswith('update') and (('=' not in sql) or  ('where' not in sql)): # 耗时50s
	            #elif sql.startswith('update') and 'where' not in sql: # 耗时43s
	                return {'code':'12309', 'msg':'update操作必须带where条件，一次只能修改一条数据'}
                elif self.sql.startswith('create') or self.sql.startswith('alter') or self.sql.startswith('drop') or sql.startswith('truncate'):
                    return {'code':'12310', 'msg':'只能进行select/insert/update/delete操作'}
                else:
                    self.conn.commit()
                    # ret = 'Done'
                    ret = {'code':'12200', 'msg':'数据操作成功'}
            return ret
        finally:
            self.cur.close()
            self.conn.close()
if __name__ == '__main__':
    sql = "select * from user t where t.name = 'uncleyong'"
    ret = DbOperate(sql).db_operate()
    print(ret)