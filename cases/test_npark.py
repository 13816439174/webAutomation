# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/28 下午5:31
# @File: test_npark.py
import unittest
from selenium import webdriver
from page_object.login_page import LoginPage
from page_object.dashboard_page import DashboardPage
from ddt import ddt,file_data
from cases.chrome_options import Options

'''
如果不希望用例之间产生关联，那就是不同的流程，用不同的测试用例，将需要的页面对象分别实例化
如果想快速的实现整个流程的覆盖测试，则通过一套driver全部实现

在unittest场景下，自定义的断言是不会有效果的
'''
@ddt()
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=Options().options_conf())
        cls.lp = LoginPage(cls.driver)
        cls.dashboard = DashboardPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/loginUserData.yaml')
    def test_01_login(self,**kwargs):
        self.lp.login(kwargs['username'],kwargs['password'])
        # self.assertEqual()

    def test_02_dashboardView(self):
        self.dashboard.viewDashboard()



if __name__ == '__main__':
    unittest.main()

