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
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(options=Options().options_conf())
driver.implicitly_wait(10)
# 实现在百度首页，鼠标悬停在"设置"按钮上
driver.get('http://www.baidu.com')
# 悬停操作：在执行过程中鼠标不能动
el = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
action = ActionChains(driver)
action.move_to_element(el).perform()
# 显示等待，通过显示等待来做assert，等到某个元素出现后，再进行下一个操作
WebDriverWait(driver,5,0.5).until(lambda el: driver.find_element_by_link_text('地图'),message='百度页面打开失败')

driver.quit()


