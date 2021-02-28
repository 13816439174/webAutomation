# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/28 下午3:07
# @File: dashboard_page.py
from base.base_page import BasePage

class DashboardPage(BasePage):
    url = BasePage.url +'project/dashboard'

    def viewDashboard(self):
        self.open()
