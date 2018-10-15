#!/bin/bash
#sendEmail下载地址http://caspian.dotconf.net/menu/Software/SendEmail/sendEmail-v1.56.tar.gz，
#可执行文件放在/usr/local/bin/
to=$1
subject=$2
body=$3
sender=
smtp_server=
user=
password=
logfile=/var/log/zabbix/mail.log
/usr/local/bin/sendEmail -o message-content-type=html -o message-charset=utf8 -f $sender -t "$to" -s $smtp_server -xu $user -xp $password -u "$subject" -m "$body"   -l $logfile
