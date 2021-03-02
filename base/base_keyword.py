# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/2 下午10:27
# @File: base_keyword.py

'''
基类，在基类中定义常规的元素操作行为及driver操作行为
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
'''
    生成一个浏览器（webdriver对象）：反射机制
    getattr(class, name)函数，从class对象中获取名称为name的成员属性
    如果要获取class对象的函数，则需要在末尾添加一个（)
    getattr(webdriver,'Chrome') == webdirver.Chrome
    getattr(webdriver,'Chrome')() == webdirver.Chrome()
    '''
def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver

class WebKeys:
    # driver = webdriver.Chrome()

    url = 'https://ctfdev.iotspacex.com/web/en/#/'

    # 构造函数
    def __init__(self,type_):
        self.driver= browser(type_)
        self.driver.implicitly_wait(10)

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

    # 文本断言校验
    def assert_text(self,loc,actual_text):
        text = self.locator(loc).text
        assert text == actual_text, '断言失败'

    # 强制等待
    def wait(self,time_):
        sleep(time_)

    # 显示等待
    def visit_wait(self, time_, loc):
        return WebDriverWait(self.driver,time_,0.5).until(lambda el: self.locator(loc),message='查找元素失败')
