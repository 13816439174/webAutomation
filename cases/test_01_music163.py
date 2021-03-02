# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/28 下午5:56
# @File: test_01_music163.py

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://music.163.com')
# 窗体最大化
driver.maximize_window()

# a 标签的元素，可以使用find_element_by_link_text
# driver.find_element_by_link_text('登录').click()
driver.find_element_by_xpath('//a[@data-action="login"]').click()
time.sleep(3)
driver.find_element_by_link_text('选择其他登录模式').click()
time.sleep(2)
driver.find_element_by_id('j-official-terms').click()
driver.find_element_by_link_text('QQ登录').click()
# 获取浏览器句柄
handles = driver.window_handles
print(handles)
# 切换到第二个页面
driver.switch_to.window(handles[1])
print(driver.title)
time.sleep(3) 
# 定位到页面的iframe中
iframe = driver.find_element_by_id('ptlogin_iframe')
driver.switch_to.frame(iframe)

# ff = driver.switch_to.frame('ptlogin_ifram')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('1053985022@qq.com')
driver.find_element_by_id('p').send_keys('happyjsn')
driver.find_element_by_id('login_button').click()
'''
句柄最好控制在2个页面之内，不超过3个页面
'''
# 切换到第一个页面
driver.switch_to.window(handles[0])
# 关闭当前句柄页
driver.close()
# 关闭整个webdriver，释放进程
driver.quit()


