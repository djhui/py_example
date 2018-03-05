#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
def Test():
    for i in range(1,100,1):
        print (i*2/3-4+6**2),


if __name__ == '__main__':
    starttime = time.time()
    for i in range(1,4):
        Test()
    print ("1,Used time:", time.time()-starttime)

    starttime = time.time()
    for i in range(1,4):
        t = threading.Thread(target=Test)
        t.start()
        t.join()
    print ("2,Used time:", time.time()-starttime)



