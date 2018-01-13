#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
from hashlib import md5

def md5_file(name):
    m = md5()
    a_file = open(name, 'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
def listyoudir(level, path):
    for i in os.listdir(path):
        try:
            print (i , md5_file(path+ '\\' + i))
        except:pass
        if os.path.isdir(path + '\\' + i):
            try:listyoudir(level+1, path + '\\' + i)
            except:pass

if __name__ == "__main__":
    try:rootpath = sys.argv[1]
    except:rootpath='.'
    try:listyoudir(0, rootpath)
    except:pass
