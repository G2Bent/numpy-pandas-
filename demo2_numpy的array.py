#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/23 15:04
# @Email   : 944921374@qq.com
# @File    : demo2.py
# @Description:
import numpy as np
import pandas as pd
#以列表形式创建一个列表
a = np.array([2,23,4],dtype=np.int)
b = np.array([2,23,4],dtype=np.float)
#输出是32位的int
print(a.dtype)
#输出6位的float
print(b.dtype)

#定义一个二维的array
array = np.array([[2,22,3],
                  [3,33,4]])
print(array)

#定义一个全部为零的数列,全部为1就ones,还有一个empty(什么都没有，几乎为零)的方法
array_zero = np.zeros((3,4),dtype=np.int)
array_empty = np.empty((3,4))
#跟python中的range的方法一样
array_arange = np.arange(12).reshape(3,4)#重新生成一个3行4列的数组
a_linspace = np.linspace(1,10,5)#从1到10的20段数列
a_linspace_reshape = np.linspace(1,10,20).reshape((1,2))#随意修改行列
print(array_zero.dtype)
print(array_empty)
print(array_arange)
print(a_linspace)
print(a_linspace_reshape)