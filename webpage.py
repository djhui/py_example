#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
r = requests.get('https://www.python.org',headers=headers)
#print(r.headers)

file = open('example.txt','w')
# 'r' : 只读
# 'w' : 写入
# 'x' : 用来创建或者写入一个文件
# 'a' : 追加
# 'r+' : 读写在同一个文件中

file.write(r.text)
file.close()