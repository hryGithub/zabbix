#!/usr/bin/python
# -*- coding: utf-8 -*-
# comment: zabbix微信报警

import requests
import sys
import json

corpid = ''  # 企业号标识
appsecret = '' # 密钥
agentid = 1000002   #应用id
partyid = "1"   #部门id

def alert(touser, subject, message, partyid=1):
    # 获取accesstoken
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + appsecret
    req = requests.get(token_url)
    accesstoken = req.json()['access_token']

    # 发送消息
    msgsend_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + accesstoken

    message = subject + "\n\n" + message
        
    params = {
        "touser": touser,
        "toparty": partyid,
        "msgtype": "text",
        "agentid": agentid,
        "text": {
            "content": message
        },
        "safe": 0
    }

    req = requests.post(msgsend_url, data=json.dumps(params))


if __name__ == "__main__":
    alert(sys.argv[1], sys.argv[2], sys.argv[3], partyid)