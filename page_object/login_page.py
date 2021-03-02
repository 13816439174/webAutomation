# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/27 下午8:29
# @File: login_page.py
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(BasePage):
    # 封装页面url:每一个不同的页面对象，对应的都是不同页面，就会有不同的url
    url = BasePage.url+' login'
    # 页面关联元素
    user = (By.XPATH,'/html/body/ph-root/ph-login/div[2]/div/form/ia-form-control[1]/input')
    pwd = (By.XPATH,'/html/body/ph-root/ph-login/div[2]/div/form/ia-form-control[2]/ia-password/input')
    button = (By.XPATH,'/html/body/ph-root/ph-login/div[2]/div/form/ia-button/button/span')

    # 页面元素的操作行为
    def login(self, username, password):
        self.open()
        self.input_(self.user,username)
        self.input_(self.pwd,password)
        self.click(self.button)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    user = 'oliviajin@abc.com'
    pwd = 'Aa123456789$'
    lp.login(user,pwd)