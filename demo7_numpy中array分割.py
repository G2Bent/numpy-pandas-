#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 9:10
# @Email   : 944921374@qq.com
# @File    : demo7.py
# @Description:
import numpy as np

A = np.arange(12).reshape((3,4))
print(A)
#竖向分割
print(np.split(A,2,axis=1))
#横向分割
print(np.split(A,3,axis=0))
#上面的只能平等分割，所以，我们需要做不等分割的方法
print(np.array_split(A,3,axis=1))

#另外一种方法对数组进行分割
#纵向分割
print(np.vsplit(A,3))
#横向分割
print(np.hsplit(A,2))

