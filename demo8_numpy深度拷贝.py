#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 9:24
# @Email   : 944921374@qq.com
# @File    : demo8.py
# @Description:numpy 赋值
import numpy as np

A = np.arange(4)
print(A)
B = A
C = A
D = B
print(D)
A[0] = 22
print(A)
print(B is A)
D[1:3] = [33,44]
print(D)

#只想用到A的值，不想关联A；那就用拷贝
B = A.copy()
print(B)

A[2] = 99
print(A)
print(B)