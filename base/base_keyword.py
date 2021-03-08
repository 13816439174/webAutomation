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
from base.log import log_option
from cases.chrome_options import Options

'''
    生成一个浏览器（webdriver对象）：反射机制
    getattr(class, name)函数，从class对象中获取名称为name的成员属性
    如果要获取class对象的函数，则需要在末尾添加一个（)
    getattr(webdriver,'Chrome') == webdirver.Chrome
    getattr(webdriver,'Chrome')() == webdirver.Chrome()
    '''
def browser(type_):
    try:
        driver = getattr(webdriver, type_)(options=Options().options_conf())
    except Exception as e:
        print(e)
        driver = webdriver.Chrome(options=Options().options_conf())
    return driver

class WebKeys:
    # driver = webdriver.Chrome()

    url = 'https://ctfdev.iotspacex.com/web/en/#/'
    log = log_option()
    # 构造函数
    def __init__(self,type_):
        # self.log.info('访问的浏览器类型是：'+type_)
        self.driver= browser(type_)
        # 隐式等待
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self,**kwargs):
        # self.log.info('访问的URL是：'+kwargs['txt'])
        self.driver.get(kwargs['txt'])

    # 定位元素
    def locator(self,**kwargs):
        # self.log.info('定位的元素是：'+kwargs['name']+'>>>'+kwargs['value'])
        return self.driver.find_element(kwargs['name'],kwargs['value'])

    # 输入
    def input(self,**kwargs):
        # self.log.info('clear输入框内容')
        el = self.locator(**kwargs)
        el.clear()
        # self.log.info('输入的内容是：'+kwargs['txt'])
        el.send_keys(kwargs['txt'])

    # 点击
    def click(self,**kwargs):
        self.log.info('点击操作')
        self.locator(**kwargs).click()

    # 切换到iframe
    def switch_to_iframe(self,**kwargs):
        # self.log.info('切换到iframe')
        iframe = self.locator(**kwargs)
        self.driver.switch_to.frame(iframe)

    # 文本断言校验
    def assert_text(self,**kwargs):
        # self.log.info('文本断言校验')
        try:
            text = self.locator(**kwargs).text
            # self.log.info('实际值的内容是：'+text)
            # self.log.info('期望值的内容是：'+kwargs['expect'])
            # self.log.info('期望值内容:{0} = 实际值内容:{1}'.format(kwargs['expect'],text))
            assert text == kwargs['expect']
            return True
        except:
            self.log.info('期望值内容:{0} != 实际值内容:{1}'.format(kwargs['expect'],text))
            return False

    # 获取元素的属性，进行断言
    def assert_attribute(self,**kwargs):
        text = self.locator(**kwargs).get_attribute(kwargs['txt'])
        try:
            assert text == str(kwargs['expect'])
            return True
        except:
            self.log.info('期望值内容:{0} != 实际值内容:{1}'.format(kwargs['expect'], text))
            return False


    # 强制等待
    def wait(self,**kwargs):
        # self.log.info('强制等待')
        sleep(kwargs['txt'])

    # 退出
    def quit(self,**kwargs):
        # self.log.info(' 退出浏览器')
        self.driver.quit()

    # 显示等待：等待到了就返回元素，等待失败就返回一个超时的异常
    def assert_wait(self, **kwargs):
        try:
            # self.log.info('显示等待')
            return WebDriverWait(self.driver,kwargs['txt'],0.5).until(
                lambda el: self.locator(kwargs['name']),kwargs['value'],message='查找元素失败')
        except:
            # log
            # self.log.info('断言显示等待失败，没有等到元素可见')
            return False

    # 切换句柄：关闭标签页，再切换
    def switch_with_close(self, **kwargs):
        handles=self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 切换句柄：不关闭标签页，直接切换
    def switch_tab_no_close(self,**kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 切换到旧窗体
    def switch_to_old_tab(self,**kwargs):
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[0])



