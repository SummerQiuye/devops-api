from email.utils import formataddr

from flask import request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "it@hunteron.com"  # 用户名
mail_pass = "zV4iF0LXHfnEuA"  # 口令


def sendMail(mail, mailHeader, mailData):
    receiverMail = [mail]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    mail_msg = f"""{mailData}"""
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = formataddr(["运维", mail_user])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    message['To'] = formataddr([mail.split("@")[0], mail])

    message['Subject'] = Header(mailHeader, 'utf-8')

    try:
        print("准备发送邮件")
        smtpObj = smtplib.SMTP_SSL(mail_host, port=465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receiverMail, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
        return jsonify({"msg": "ok", "data": "send mail success"})
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
        return jsonify({"msg": "err", "data": "send mail failed"})


# mailContent = '''
# <p>你好，后台已重置你的LDAP账户密码，<br/>新密码为：</p>
# <p>34vbivb</p>
# '''
# sendMail(mail="qiuye@novelpro.cn", mailHeader="忘记密码找回", mailData=mailContent)
