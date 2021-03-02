# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/2 下午8:32
# @File: test_03_actionChains.py
'''
鼠标悬停，元素悬停
from selenium.webdriver import ActionChains
通过ActionChains模块来实现

'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from cases.chrome_options import Options

driver = webdriver.Chrome(options=Options().options_conf())
driver.implicitly_wait(10)
# 实现在百度首页，鼠标悬停在"设置"按钮上
driver.get('http://www.baidu.com')
# 悬停操作：在执行过程中鼠标不能动
el = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
action = ActionChains(driver)
action.move_to_element(el).perform()
driver.quit()


