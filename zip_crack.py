#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zipfile

def zip_crack():
    file = zipfile.ZipFile(r'zip_crack.zip')
    for i in range(1000,2000,1):
        try:
            file.extractall(path=r'./', pwd=bytes(str(i).encode('utf-8')))
            print ("Cracked, password is: %s" %i)
            break
        except :
            print("try password %s" % i)

if __name__ == '__main__':
    zip_crack()