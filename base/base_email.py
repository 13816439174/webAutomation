# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/3/14 下午6:15
# @File: base_email.py
'''
smtp：是一种简单的邮件传输协议
smtplib：封装了smtp协议，对于邮件发送就更加简单了

'''

import smtplib
# 发送文本的方法
from email.mime.text import MIMEText
# 发送附件
from email.mime.multipart import MIMEMultipart
# 设置头部内容
from email.header import Header
# 图片附件
from email.mime.image import MIMEImage

# 创建邮箱服务器连接: 比喻成邮局
# 163: smtp.163.com
# qq: smtp.qq.com , 465->ssl, 587->not ssl
# smtplib.SMTP 也可以
# smtplib.SMTP_SSL(邮箱连接地址，端口号)
con = smtplib.SMTP_SSL('smtp.qq.com','465')

# 登录邮箱，用户名和密码
# 163：用户名和密码，直接填写163邮箱的账号和密码
# qq: 用户名=邮箱号，密码=授权密码
con.login(user='415610507@qq.com',password='gmlljedprdglbhfg')

# 发送者
sender = '415610507@qq.com'
# 接受者
# receiver = ['415610507@qq.com','1053985022@qq.com']
receiver = '415610507@qq.com'
htmlContent = '''
<!doctype html><!--生命当前文档类型-->
<html><!--网页结构的开始-->
    <head><!--描述网页基本信息-->
        <meta charset="UTF-8"><!--声明网页编码格式-->
        <meta name="Keywords" content="关键字，关键词">
        <meta name="Description" content="描述和简介">
        <title></title>
    </head>
    <body>
        <p>html主题</p>
        <h1>主题标签</h1>
    </body>
</html>
'''


# 准备发送邮件 _text= 邮件正文  _subtype= 文件类型（文本，html, base64(二进制类型)）, plain默认就是纯文本. _charset= 编码格式
# message = MIMEText(_text='邮件正文',_subtype='plain',_charset='utf-8')      #发送文本邮件
message = MIMEText(_text=htmlContent,_subtype='html',_charset='utf-8')       #发送html邮件

# 发送附件
# 实例化附件，创建一个信封
message1 = MIMEMultipart()
# 文件在哪 rb读 wb写
content = open('../data/qqEmailLogin.xlsx','rb').read()
# print(content)
# 把读取出来的内容放在文本中 信纸
# file1 = MIMEText(_text=content,_subtype='base64',_charset='utf-8')
file1 = MIMEText(content,'base64','utf-8')
# 給信纸取名字
file1['Content-Disposition']='attachment;filename="qqEmailLogin.xlsx"'
# 把信纸放到信封中
message1.attach(file1)

# 添加邮件正文
msg = MIMEText('我是邮件征文')
message1.attach(msg)

# 添加图片附件
image = open('../data/1.png','rb').read()
image_data = MIMEImage(image)
image_data['Content-Disposition']='attachment;filename="1.png"'
message1.attach(image_data)

# 设置头部内容
# 设置头部标题
message1['Subject']=Header('附件标题','utf-8')
# 发件人
message1['From']=Header('着凉专家<415610507@qq.com>','utf-8')
# 收件人
message1['To']=Header('着凉专家2','utf-8')
# 发送邮件
# con.sendmail(sender,receiver,message.as_string())

con.sendmail(sender,receiver,message1.as_string())


