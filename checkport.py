#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗

import socket
import threading
from config import ports,nodes
import time

# 定义检查端口
def checkport(ip,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)
    try:
        sk.connect((ip, port))
        print '%s port %d OK!' % (ip,port) ,
    except Exception:
        print '\033[1;33;44m%s port %d not connect!\033[0m' % (ip, port)
    sk.close()

#checkport('13.125.29.205',7000)


#nodes=["18.195.110.47",]




def ch(x):
    for i in ports:
        t = threading.Thread(target=checkport,args=(x,i))
        t.start()
    t.join()


map(ch, nodes)