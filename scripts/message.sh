#!/bin/bash
#短信报警
message=`echo $3|sed 's/ /%20/g'`#url处理，空格用%20替换
time=`date "+%Y-%m-%d %H:%m:%s"`
url=
result=$(curl "$url")
echo "时间:$time                        收件人:$1">> /var/log/zabbix/message.log
echo "短信内容:$3" >> /var/log/zabbix/message.log
echo "状态:$result" >> /var/log/zabbix/message.log
echo "--------------------------------------------">> /var/log/zabbix/message.log

