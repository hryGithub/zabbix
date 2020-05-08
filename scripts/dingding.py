#!/usr/bin/python
# -*- coding: utf-8 -*-
# comment: zabbix钉钉报警

import requests
import json
import sys
import os

headers = {'Content-Type': 'application/json'}

#钉钉机器人地址

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=8ea7abd3db4b49a9e898e911920d4899c526ae78f5794c977cfca8b6c0bjsdd'

def msg(user, text):
    data = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [user],
            "isAtAll": False
        }
    }
    print(requests.post(url=webhook, data=json.dumps(data), headers=headers))
    # if os.path.exists("/usr/local/zabbix/log/dingding.log"):
    #     f = open("/usr/local/zabbix/log/dingding.log", "a+")
    # else:
    #     f = open("/usr/local/zabbix/log/dingding.log", "w+")
    # f.write("\n" + "--" * 30)
    # if x.json()["errcode"] == 0:
    #     f.write("\n" + str(datetime.datetime.now()) + "    " + str(user) + "    " +
    #             "发送成功" + "\n" + str(text))
    #     f.close()
    # else:
    #     f.write("\n" + str(datetime.datetime.now()) + "    " + str(user) + "    " +
    #             "发送失败" + "\n" + str(text))
    #     f.close()


if __name__ == "__main__":
    msg(sys.argv[1], sys.argv[3])