#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/23 15:51
# @Email   : 944921374@qq.com
# @File    : demo5.py
# @Description:索引，根据位置找到对应的值
import numpy as np

A = np.arange(3,15)
print(A)
print(A[3])
B = A.reshape((3,4))
print(B)
print(B[1][1])
print(B[2][1])
print(B[2,:])#输出第三行所有数
#只能输出行，不能输出列，另一种方法输出列
for row in B:
    print(row)
#这是输出列，每一个迭代出来
for col in B.T:
    print(col)

#迭代出项目，只输出一行
for item in B.flat:
    print(item)

