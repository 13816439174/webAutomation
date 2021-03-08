# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/4 下午2:21
# @File: test_04_qqEmailLogin.py

from selenium import webdriver
from cases.chrome_options import Options
from base.base_keyword import WebKeys
#
driver = webdriver.Chrome(options=Options().options_conf())
url = 'https://mail.qq.com/'
driver.get(url)
iframe = driver.find_element_by_id('login_frame')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//*[@id="u"]').send_keys('1053985022@qq.com')
driver.find_element_by_id('p').send_keys('happyjsn11')
driver.find_element_by_id('login_button').click()
driver.find_element_by_link_text()
driver.quit()


