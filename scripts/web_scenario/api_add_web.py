#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pyzabbix import ZabbixAPI
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ZABBIX_SERVER = "http://13.230.116.168/zabbix/"
USER = "Admin"
PASSWORD = "zabbix"
HOSTNAME = "Zabbix server"
#URL = "http://soa.wex101.local/ues-ws/service"
APPLICATION = "web监测"


def login(ZABBIX_SERVER, USER, PASSWORD):
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login(USER, PASSWORD)
    return zapi


def gethostid(auth, HOSTNAME):
    request = ZabbixAPI.do_request(auth, 'host.get', params={"filter": {"host": HOSTNAME}})
    if request['result']:
        return request['result'][0]['hostid']
    else:
        print("找不到该主机")
        sys.exit(1)


def getapplicationid(auth, hostid):
    try:
        request = ZabbixAPI.do_request(auth, 'application.create', params={"name": APPLICATION, "hostid": hostid})
    except Exception as e:
        print(e)
    request = ZabbixAPI.do_request(auth, 'application.get', params={"hostids": hostid})
    for num in range(0, len(request['result'])):
        if request['result'][num]['name'] == APPLICATION:
            return request['result'][num]['applicationid']


def create_web_scenario(auth, NAME, URL, status_code, hostid, applicationid):
    request = ZabbixAPI.do_request(auth, 'httptest.get', params={"filter": {"name": NAME}})
    if request['result']:
        print('该web监控已经添加过了')
    else:
        try:
            ZabbixAPI.do_request(auth, 'httptest.create', params={"name": NAME, "hostid": hostid, "applicationid": applicationid, "delay": '1m', "retries": '3', "steps": [{'name': NAME, 'url': URL, 'status_codes': status_code, 'no': '1'}]})
        except Exception as e:
            print(e)


def create_trigger(auth, HOSTNAME, NAME, URL):
    expression = "{"+"{0}:web.test.fail[{1}].last()".format(HOSTNAME, NAME)+"}" + "<>0"
    try:
        ZabbixAPI.do_request(auth, 'trigger.create', params={"description": NAME + " test failed!", "expression": expression, "priority":5})  
    except Exception as e:
        print(e)


auth = login(ZABBIX_SERVER, USER, PASSWORD)
hostid = gethostid(auth, HOSTNAME)
applicationid = getapplicationid(auth, hostid)

with open(os.path.join(BASE_DIR, "wealth_web_check.txt"), encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        tmp = line.split()
        name = tmp[0]
        url = "http://" + tmp[1]
        status_code = tmp[2]
        # print(name, url, status_code)
        create_web_scenario(auth, name, url, status_code, hostid, applicationid)
        create_trigger(auth, HOSTNAME, name, url)