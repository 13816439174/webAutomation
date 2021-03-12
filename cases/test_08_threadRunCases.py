# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/12 下午1:28
# @File: test_08_threadRunCases.py

from base.read_excel import read_excel
import os
import threading

if __name__ == '__main__':
    case = []
    th = []
    for path,dir,files in os.walk(r'../data/'):
        for file in files:
            excel_path = path+file
            s = os.path.splitext(file)[1]
            # print(s)
            if s == '.xlsx':
                case.append(file)
                t = threading.Thread(target=read_excel,args=[excel_path])
                th.append(t)
            else:
                print('该文件无法识别：'+file)

    for i in th:
        i.start()