import unittest
from ddt import *

@ddt
class Test001(unittest.TestCase):

    lis = ["001","002","003"]

    def save_date(self,source,key,jexpr):
        '''
        提取参数并保存至全局变量池
        :param source: 目标字符串
        :param key: 全局变量池的key
        :param jexpr: jsonpath表达式
        :return:
        '''
        pass

    for i in lis:
        di = [{'descrption': '登入接口', 'url': 'https://staging-api.creams.io/oauth/token/password', 'method': 'POST', 'headers': '{\n "Authorization": "",\n "Content-type": "application/json;charset=UTF-8",\n"Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiT0F1dGgyIiwiQ1JFQU1TIl0sIm9wZW5faWQiOiJjcmVhbXNvNjhhMzdiMGIzY2M5NGI2MjkyNGYzOWIyYWY2YTk3MDYiLCJ1c2VyX25hbWUiOiJjcmVhbXNuY2VkNmY3YjdjOTAxNDk1OGIzOTM3NGIyOGVlNTJiZjIiLCJzY29wZSI6WyJDUkVBTVMiXSwidW5pb25faWQiOiJjcmVhbXN1YzkxODJkODFmMTI4NDhjZWIyZGUxMjQ3MmViNjVkODciLCJleHAiOjE1Njc0MzczMjEsImF1dGhvcml0aWVzIjpbIk5PUk1BTCJdLCJqdGkiOiJmZDVlN2ZmOC1hZDA0LTQ0N2YtOTE0NS0xOTE5NDQ4MjRjNDYiLCJjbGllbnRfaWQiOiJjcmVhbXNfd2ViX2FwcCJ9.adHSOs3CuPJiV8K7IuFnBF1LwOe8Tz1ylKJPt53F8k3U8McW-Lo7UHYaR8tekUjO6o0YMdH7eu8RYAw877c-GQqHVwSgI_pSG3huDeY9zKB2irFhB8efcBUSWTJMExpKbDAEpQxDvZLd_cxYrDktc1Cdl6g2tIcPsBXNeyUlgdKCf6ZXd094kQ1SH-HwQtlf5VAdhOtNK-scmlLHejjEbSfhy-ANtAiyOrRHodU2blyNEqXB_ogE3bg5J14zH1_QtUT55VDHcxc7ooYB9VeYrs6sIkv9PUI6sLq5oqI-edHiHpdb9Jvrm3UeIcAXHVZhDknZpId7PAHFomxg0LnV0A"\n}', 'cookies': '', 'params': '{\n "client_id": "creams_mobile_app",\n "password": "Creams820",\n "username": "17826826147"\n}', 'body': '', 'file': '', 'verify': '$.scope=CREAMS;$.token_type=Bearer', 'saves': 'token=$.access_token', 'dbtype': 'mysql', 'db': '', 'setup_sql': '', 'teardown_sql': ''}, {'descrption': '查询全部楼宇', 'url': 'https://staging-api.creams.io/web/buildings', 'method': 'GET', 'headers': '{"Authorization":"Bearer ${token}"}', 'cookies': '', 'params': '', 'body': '', 'file': '', 'verify': '$.items[0].province.name=北京市', 'saves': '', 'dbtype': '', 'db': '', 'setup_sql': '', 'teardown_sql': ''}]
        exec('''
@data(*{})
@unpack
def test_{}(self,descrption,url,method,headers,cookies,params,body,file,verify,saves,
                                                                            dbtype,db,setup_sql,teardown_sql):
    print(descrption,url,method,headers,cookies,params,body,file,verify,saves,
                                                                            dbtype,db,setup_sql,teardown_sql)     
        
        '''.format(di,i))


