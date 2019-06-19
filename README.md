# 接口自动化框架         作者:楷楷

## 项目说明
- 本框架是为了快速实现**http/https**协议而设计的一套数据驱动自动化接口框架,基于**EXCEL+requests+unittest+ddt**设计,**pytest**作为执行器,本框架无需你使用代码编写用例,那你可能
会担心万一有接口之间相互依赖,或者说需要登入的token等之类的接口,该如何编写用例,在这里告诉你们笨框架已经完美解决此问题,所有的一切将在EXCEL中进行！！本框架实现了在EXCEL中
进行**接口用例编写,接口关联,接口断言**,还有很重要的一点,实现了类似**jmeter函数助手**的功能,譬如生成UUID,随机定长字符串,格式化日期,正则表达式等,只需要你在EXCCEL中使用特殊的写法就能够使用这些函数啦~~是不是很期待！！


## 技术栈
- requests
- unittest
- pytest
- pytest-html
- xlrd
- logging
- 函数助手


## 环境部署
- 解压压缩包，使用pycharm打开项目文件
- 进入**File - Settings - Project - Project Interpreter**,选择项目中的 **ApiTestFrameWork/venv** 作为虚拟环境,若无法使用,可以尝试新增虚拟环境后,在控制台cd到**venv/Scripts**下,使用命令**pip install -r requirements.txt**文件所在的绝对路径（在项目根目录）,一条命令安装好所有依赖环境,你要做的就是慢慢等它装好
- 验证环境是否安装完毕
- **File - Settings - Tools - Python Integrated Tools - Default Test Runner**选择**py.test**
- 执行**runCase.py**,观察结果是否成功,excel中有一条访问百度的用例,可以看看执行结果百度是否访问成功
- 查看report下是否有测试报告生成

## 项目结构说明
- conf ===========> 配置文件
- core ===========> 公共方法,工具类等
- db_operate ==========> 数据库相关方法封装
- files ==========> 测试文件
- logs ==========> 日志文件
- report ==========> 测试报告
- test_case ===========> 测试用例
- venv ============> 虚拟环境
- requirements.txt ============> 相关依赖包文件
- runCase.py =============> 测试用例执行器
- READMD.md ============> 项目说明文档

## EXCEL字段说明
- **description**:用例描述
- **url**:接口地址
- **method**:请求方式(目前只支持GET,POST)
- **headers**:请求头,格式为 {"key","value"}
- **cookies**:Cookies就是Cookies啦,格式为 {"key":"value"}
- **params**:请求参数,注意是参数而不是请求体,类似url后拼接的?key=value&key=value,格式为 {"key":"value"}
- **body**:请求体,格式为 {"key":"value"}
- **file**:请求文件,格式为 {"key":"文件名称"}  注意此时文件需放到框架的files目录下才能读取
- **verify**:断言,格式为  JSONPATH=预期结果 
- **saves**:关联,格式为 自定义key=JSONPATH
- **dbtype**:数据库类型,目前支持mysql/redis
- **db**:数据库名称
- **setup_sql**:前置数据库语句(在用例执行前执行),若为mysql,直接写sql即可,可支持执行多条sql,用分号隔开,若是查询语句则会将查询的字段存储到公共变量池;若数据库类型为redis,则写形如key1;key2;key3,会进行redis查询并储存变量
- **teardown_sql**:后置数据库语句(在用例执行后执行),用法如上


## 关联详解
- 公共参数池:意思就是你可以存储接口的响应值到参数池中,以便后续接口使用
- 如何将响应字段存到参数池:在EXCEL中saves列,使用格式形如 **key=JSONPATH**  填写,支持多字段存储,使用英文分号隔开 , 举栗子:**id=$.object.id;code=$.code**
学过jmeter的朋友们应该知道,类似里面的jsonpath提取器
- 下个接口如何使用已经存储的参数:在下个接口入参中使用形如  **${key}** 的格式,提取参数池中的key对应的value即可,当然你必须保证前面的用例已经存储过该key

## 断言详解
- 在verify中填写形如  **JSONPATH=预期结果** ,框架会根据该JSONPATH从响应JSON中提取目标字段,和预期结果进行比对,同样支持多断言,举栗子:**$.msg=操作成功;$.code=100000**

## 函数助手详解
- 说明:函数助手是来自Jmeter的一个概念,有了它意味着你能在EXCEL中使用某些函数动态的生成某些数据,如随机定长字符,格式化日期,UUID,正则表达式等等
- 目前支持的函数助手:
- MD5(arg)  =========》 md5加密字符串,arg为待加密的字符串
- UUID() ==========》 生成UUID
- RANDOWINT(length) =========》 生成定长纯数字字符串,length为字符串长度
- RANDOMSTR(length) =========》 生成定长  数字+大小写字母组合 的字符串,length为字符串长度
- NOW(format,hours) =========》 生成当前日期,format为日期格式,默认为  %Y-%m-%d %H:%M:%S ,可根据自己的需求修改,hours为小时偏移量  如 hours=1 代表当前时间加一小时,支持负数
- REGEX(targetstr,pattern,index) =========》 正则提取器,targetstr为目标字符串,pattern为正则表达式,index为索引,意味着如果有多个匹配结果,你要提取你取到的第几个值,默认索引为0

### 如何在EXCEL中使用
- 使用双下划綫开头,举栗子  **{"key":"__UUID()"}**  读取到框架里就会成  **{"key":"e4122e2a-4604-4875-9e5f-7e81434665d0"}**  

### 函数助手注意事项
- 参数为字符串的记得加**引号！！！** 中英文引号别搞混啦，统一用英文引号，就像写代码一样

## 待优化
- 用例控制器 Y/N
- 用例集相互隔离,若其中一条用例执行失败,则不会执行后续用例,一个流程视为一个用例集
- excel表中多个Sheet批量读取
- jenkins集成
- 更多后续。。如flask可视化展示页面开发
