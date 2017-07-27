#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

# import smtplib # 操作smtp服务器模块
# from email.mime.text import MIMEText  # 用来封装邮件内容
# from email.header import Header
#
# #邮件内容
# content = r"this only our python test, 这是个测试邮件"
#
# # 封装邮件
# msg = MIMEText(content, "plain", "utf-8")
#
# # 收件人名单
# msg_to_str = """
# liupanfei001@sinatay.com,
# """
# # 邮件头部定义
# mail_from = "505567802@qq.com"
# msg["Subject"] = "email test"
# msg["From"] = mail_from
# msg["to"] = msg_to_str
#
# # 登入邮件服务器
# # msg_to_list = msg_to_str.replace('\n', "").split(',')
# # print(msg_to_list)
# server = smtplib.SMTP_SSL("smtp.qq.com", 465)
# server.login(mail_from, "ovohtljpytfabhdc")
#
# # 发送邮件
# server.sendmail(mail_from, msg["to"] , msg.as_string())
# server.quit()

from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mail_info = {
    "from": "505567802@qq.com",
    "to": ['liuchen001@sinatay.com', 'liupanfei001@sinatay.com', 'songjun@sinatay.com', 'hzsongjun@hotmail.com', ],
    "hostname": "smtp.qq.com",
    "username": "505567802@qq.com",
    "password": "ovohtljpytfabhdc",
    "mail_subject": "Email Test",
    "mail_text": "hello, this is a test email, 这是个测试邮件",
    "mail_encoding": "utf-8"
}

if __name__ == '__main__':
    # 这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"])
    # smtp.set_debuglevel(1)

    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])

    msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = ','.join(mail_info["to"])
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

    smtp.quit()