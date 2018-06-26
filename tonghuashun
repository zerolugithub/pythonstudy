#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 15:19
# @Author  : zero
# @File    : tonghuashun.py
# @Software: PyCharm

import random

# 为黑桃（Spade）、红桃（Heart）、方块（Diamond）、梅花（Club）
flower = ["Spade","Heart","Diamond","Club"]

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
test = []
tt = []
tt2 = []
fiveCount = []

def tonghuashun():
    for i in numbers:
        for j in dict.fromkeys(flower,i).iteritems():
            test.append(j)
    for i in range(5):
        fiveCount.append(random.choice(test))
    # sorted(fiveCount, key=lambda x: x[0])
    print "*"*30
    print fiveCount
    print sorted(fiveCount, key=lambda x: x[0])
    print fiveCount
    fiveCount.sort()
    print fiveCount
    print "*" * 30
    for i in fiveCount:
        tt.append(i[0])
    print len(set(tt))
    if len(set(tt)) == 1:
        for i in fiveCount:
            tt2.append(i[1])
        tt2.sort()
        if tt2[4] - tt2[0] == 4:
            print "is"
    else:
        print "is not"

tonghuashun()

