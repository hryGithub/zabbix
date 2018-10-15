#!/bin/bash
to=$1
subject=$2
body=$3
sender=
smtp_server=
user=
password=
logfile=/var/log/zabbix/mail.log
/usr/local/bin/sendEmail -o message-content-type=html -o message-charset=utf8 -f $sender -t "$to" -s $smtp_server -xu $user -xp $password -u "$subject" -m "$body"   -l $logfile
