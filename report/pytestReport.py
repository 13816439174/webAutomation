# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/11 下午3:48
# @File: pytestReport.py
import pytest
import os

if __name__ == '__main__':
    # current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    # pytest.main(['-v','../test_case/test_philipsAdmin.py','--html=../test_report/pytestReport'+current_time+'.html'])

    pytest.main(['-v','../test_case/test_06_excelAndKeywordAndUnittestQmailLogin.py','--alluredir','../temp'])
    os.system('allure generate ../temp -o ../test_report --clean')