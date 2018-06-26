#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 10:24
# @Author  : zero
# @File    : shunzi.py
# @Software: PyCharm
import random


def is_shunzi(a):
    print list(set(a))
    # if len(a) <= 4:
    #     return False
    if list(set(a)) == [0]:
        return True
    hash_dict = dict()
    for i in a:
        if i == 0:
            continue
        if i in hash_dict.keys():
            return False
        else:
            hash_dict[i] = 100
    result = True if (max(hash_dict.keys()) - min(hash_dict.keys())) <= 4 else False
    print hash_dict
    return result


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,0]
data = []
for i in range(5):
    data.append(random.choice(numbers))
print(is_shunzi(data))
