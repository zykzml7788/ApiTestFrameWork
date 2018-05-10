
【更新历史】

2018-04-25 v1.2 新增数据库操作

2018-04-24 v1.1 新增日志调试日志，可屏幕和文件输出日志

2018-04-12 v1.0 基础版





【功能介绍】

bin: 可执行文件，程序入口

conf: 配置文件

core: 核心文件

db_fix: 数据库操作

log: 日志文件

reprot: 测试报告

test_case: 测试用例（数据文件），# testSelect.py文件用例对应的mock项目地址：https://github.com/UncleYong/mock_test

README.md: 说明文件





【待扩展】


集成jenkins


如果脚本在：C:\zt2

jenkins命令：

    windows下：python3 C:\zt2\bin\my_run.py %BUILD_NUMBER%

    linux下：python3 /opt/py_code/2/zt2/bin/my_run.py $BUILD_NUMBER

输出的报告名称为：【6】2017-09-11_09_09_56_report.html


