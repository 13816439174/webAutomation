# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/1 下午1:14
# @File: test_02_baiduImage.py
from selenium import webdriver
import time

driver = webdriver.Chrome()
# .maximize_window()可能会出现driver超时的问题
driver.maximize_window()
# 上传图片的写法，通过send_key 文件路径
driver.get('https://image.baidu.com')
# 隐式等待
driver.implicitly_wait(10)
time.sleep(2)
# driver.find_element_by_xpath('//*[id="sttb"]').click()
# driver.find_element_by_id('sttb').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[id="stfile"]').send_keys(r'/Users/jinshengnan/Downloads/灯杆.jpg')

# by=定位方法，value=匹配定位方法的值，这种方式在实际应用中更灵活
# driver.find_element(by='xpath',value='//*[id="stfile"]')

# assert断言，使用text来判断，例如：下面例子
expect_text = '百度首页'

# 当元素有文本信息的时候，可以通过.text来获取元素的text信息
actual_text = driver.find_element(by='xpath',value='//*[@id="new-userinfo-baiduIndex"]').text
print(actual_text)
assert expect_text == actual_text, '断言失败'

# 通过selenium获取元素属性。当元素value有值，或者class有值时，使用get_attribute来获取value,class值
expect_text1 = '百度一下'
el = driver.find_element(by='xpath',value='//*[@id="homeSearchForm"]/span[2]/input')
value = el.get_attribute('value')
print(value)
# 最重要是断言 assert
assert expect_text1 == value, '断言失败'

# 通过selenium修改元素属性
'''
JS执行器:
    Document对象的应用：Document对象是JS中的一个模块
    1. 用于获取元素信息或者修改元素属性，以便于实际自动化时可以更为便捷的执行操作
    2. JS执行期配合document对象，一般对用于自动化中的疑难杂症来进行处理的。
'''
# js = "document.getElementById('s_newBtn').setAttribute('value','asd')"
js = "document.getElementById('new-userinfo-baiduIndex').setAttribute('value','asd')"
# 执行js语句函数：js执行器
driver.execute_script(js)

js1 = "document.getElementById('new-userinfo-baiduIndex').removeAttribute('value','asd')"
driver.execute_script(js1)

# 滚动条操作
# 'document.scrollingElement.scrollTop' 表示上下滚动，0-2000区间
# window.scrollTo(x,y)左右滚动

# 如何有效的运行js
el1 = driver.find_element_by_xpath('//*[@id="new-userinfo-baiduIndex"]')
# 占位符的应用 在浏览器的console中 document语句： document.getElementsByTagName('a')[16].innerHTML='tester'
js2 = "arguments[0].innerHTML='olivia'"
driver.execute_script(js2,el1)


driver.quit()