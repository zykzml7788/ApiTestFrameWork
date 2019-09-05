#!/user/bin/env python
#coding=utf-8
'''
@project : my_rf
@author  : djcps
#@file   : readExcel.py
#@ide    : PyCharm
#@time   : 2019-05-28 11:10:44
'''
import xlrd
from conf.settings import *


def read_excel(excel_path=BASE_PATH+"/conf/case.xlsx"):
    '''
    读取excel文件内容
    :param excel_path: xlsx文件的路径
    :return: k-v的列表,k为sheet名，v为表格数据
    '''
    # 打开文件
    workbook = xlrd.open_workbook(excel_path)

    #获取所有sheet
    sheet_list = workbook.sheet_names()  # [u'sheet1', u'sheet2']

    sheets_data = []

    for sheet in sheet_list:

        # 根据sheet索引或者名称获取sheet内容

        sheet = workbook.sheet_by_name(sheet) # sheet索引从0开始

        # 获取第一行作为key
        first_row = sheet.row_values(0)  # 获取第一行内容

        # 获取表的行数
        rows_length = sheet.nrows

        #定义两个空列表，存放每行的数据
        all_rows = []
        rows_dict = []
        for i in range(rows_length):  # 循环逐行打印
            if i == 0:  # 跳过第一行
                continue
            all_rows.append(sheet.row_values(i))
        for row in all_rows:
            lis = dict(zip(first_row,row))
            rows_dict.append(lis)

        sheet_data = {"sheet":sheet.name,"data":rows_dict}
        sheets_data.append(sheet_data)

    return sheets_data


