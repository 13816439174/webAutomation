# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/4 下午4:40
# @File: excel_read.py
import openpyxl


def excel_read(self, path):
    excel=openpyxl.load_workbook()
    sheetNames=excel.sheetnames
    for name in sheetNames:
        print(name)
    sheet1=excel[name]
    for value in sheet1.values:
        print(value)
        args={}
        args['name']=value[2]
        args['value']=value[3]
        args['txt']=value[4]
        args['expect']=value[6]
        # 基于A列进行判断是否为测试用例
        if type(value[0]) is int:
            '''
            在读取关键字时，分几类情况：
            1。 关键字驱动类的实例化
            2。 断言类型的关键字
            '''
            # 判断是否实例化
            if value[1] == 'open_browser':
                wk=WebKeys(value[4])
            # 非特殊关键字，通过反射机制实现
            else:
                getattr(wk, value[1])(**args)