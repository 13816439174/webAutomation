# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/27 下午8:13
# @File: base.py
'''
基类，在基类中定义常规的元素操作行为及driver操作行为
'''

from selenium import webdriver


class BasePage:
    # driver = webdriver.Chrome()

    url = 'https://ctfdev.iotspacex.com/web/en/#/'

    # 构造函数
    def __init__(self,driver):
        self.driver= driver

    # 访问url
    def open(self):
        self.driver.get(self.url)

    # 退出
    # def quit(self):
    #     self.driver.quit()

    # 定位元素
    def locator(self,loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self,loc,txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self,loc):
        self.locator(loc).click()