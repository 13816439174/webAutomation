# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/2 下午1:55
# @File: test_alert.py

'''
网页弹窗：
1。确定弹窗 -> alert
2。 确定，取消弹窗  -> prompt
3。 输入文本，确定，取消弹窗 ->  prompt文本窗

这种弹窗的形式基本已经没有了，因为交互太老了
移动端叫toast

特殊弹窗（通知，不属于弹窗）：这类的内容，需要通过修改chrome属性来实现操作
1。 记住密码和更新密码
2。 禁用启用权限设置
3。 弹窗允许与否
'''
from selenium import webdriver

driver = webdriver.Chrome()
# 切换到弹窗本体
web_alert = driver.switch_to.alert
# 确认弹窗
web_alert.accept()
# 取消弹窗
web_alert.dismiss()
# 输入文本
web_alert.send_keys('')
# 获取文本
web_alert.text

