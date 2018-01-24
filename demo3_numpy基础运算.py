#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/23 15:18
# @Email   : 944921374@qq.com
# @File    : demo3.py
# @Description:numpy的运算
import numpy as np
#一、
a = np.array([10,20,30,40])
b = np.arange(4)
c = a-b
#平方实用双星号代替
d = b**2
#三角函数运算
e = 10*np.sin(a)
print(a)
print(b,b<3)
print(c)
print(d)
print(e)

#二、矩阵运算
a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape(2,2)
print(a)
print(b)

c = a*b
#矩阵乘法
c_dot = np.dot(a,b)
#将前面的矩阵乘后面的矩阵
c_dot_t = a.dot(b)
print(c)
print(c_dot)
print(c_dot_t)

#三、随机参数矩阵
a = np.random.random((2,3))
print(a)

#求和
print(np.sum(a,axis=1))
print(np.min(a,axis=0))#看哪一列是最小值
print(np.max(a,axis=1))#看哪一行是最大值
