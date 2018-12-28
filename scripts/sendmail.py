#!/usr/bin/python
# coding:utf-8

import smtplib
from email.mime.text import MIMEText
import sys

#  configure 
smtp_server = 'smtp.gmail.com'
sslPort = 465
mail_user = 'monitor@wex101.com'
mail_pass = 'WeX101WeX'


def send_mail(to_list, subject, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = mail_user
    msg['to'] = ','.join(to_list)

    try:
        # 普通连接
        # s = smtplib.SMTP_SSL(smtp_server)
        s = smtplib.SMTP_SSL(smtp_server, sslPort)
        s.login(mail_user, mail_pass)
        s.sendmail(mail_user, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print str(e)
        return False


if __name__ == "__main__":
    send_mail(sys.argv[1].split(","), sys.argv[2], sys.argv[3])