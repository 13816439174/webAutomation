# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/2 下午2:19
# @File: chrome_options.py

'''
浏览器配置：
1。 不显示黄条
2。 窗体最大化
3。 加载本地缓存

'''

from selenium import webdriver

# 配置ChromeOptions: 一般作为专门的配置类进行存放
class Options:
    def options_conf(self):
        # 创建options对象：专门配置浏览器的设置
        options = webdriver.ChromeOptions()

        # 去掉默认的自动化提示: 不去掉一般不会有任何影响，但在特殊情况下，黄条可能会遮挡页面内容
        options.add_experimental_option('excludeSwitches',['enable-automation'])

        # 窗体最大化: Chrome + 80版 options.add_argument('--start-maximized') 不奏效
        # options.add_argument('--start-maximized')
        # 窗体最大化：使用options.add_argument('start-fullscreen')
        options.add_argument('start-fullscreen')
        # 加载本地缓存，让浏览器变成一个有缓存的模式

        '''
        1。 通过指令查找本地的浏览器缓存 chrome://version 获得 个人资料路径：
        /Users/jinshengnan/Library/Application Support/Google/Chrome/Default
        2. 通过传入本地缓存来实现缓存的获取：参数 --user-data-dir= 
        3. 调用本地缓存时，要先关闭所有正在应用的浏览器窗体
        4. 一般不推荐使用本地缓存
        '''
        # options.add_argument(r'--user-data-dir=/Users/jinshengnan/Library/Application Support/Google/Chrome/User Data')

        # 无头模式，无页面运行，会尽可能的降低CPU的使用率
        # options.add_argument('--headless')

        # 隐身模式，没啥用，就是好玩
        options.add_argument('incognito')
        return options

# if __name__ == '__main__':
#     options = Options().options_conf()
#     driver = webdriver.Chrome(options=options)
#     driver.get('http://www.baidu.com')
#     driver.implicitly_wait(10)