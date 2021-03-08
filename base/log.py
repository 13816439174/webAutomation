# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/7 下午7:22
# @File: log.py

import logging

def log_option():
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()

    logger.addHandler(sh)

    fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
    formator=logging.Formatter(fmt=fmt)
    sh.setFormatter(formator)

    # 把日志信息输出到文件, 创建一个文件，文件在哪？

    fh=logging.FileHandler('log.log', encoding='utf-8')
    logger.addHandler(fh)
    fh.setFormatter(formator)
    return logger
