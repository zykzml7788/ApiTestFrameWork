#!/user/bin/env python
#coding=utf-8
'''
@project : my_rf
@author  : djcps
#@file   : runCase.py
#@ide    : PyCharm
#@time   : 2019-05-28 15:27:00
'''

'''
    pytest用例执行文件
'''
if __name__ == '__main__':
    import pytest
    import time
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    pytest.main(['-s','./test_case/test_case.py','--html=report/{}_report.html'.format(now)])