#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#print(os.path.join(BASE_DIR,"web_check.txt"))
for line in open(os.path.join(BASE_DIR, "wealth_web_check.txt"), encoding='utf-8'):
    tmp = line.split()
    app = tmp[0]
    url = "http://" + tmp[1]
    status = tmp[2]
    print(app, url, status)