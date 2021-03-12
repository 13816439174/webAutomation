# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/12 上午11:25
# @File: test_07_threadDemo.py

import threading
from time import sleep
from selenium import webdriver

def visit(driver):
    driver.get('http://www.baidu.com')

th = []
driver = webdriver.Chrome()
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()

th.append(threading.Thread(target=visit,args=[driver]))
th.append(threading.Thread(target=visit,args=[driver1]))
th.append(threading.Thread(target=visit,args=[driver2]))
for t in th:
    t.start()



