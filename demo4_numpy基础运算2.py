#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/23 15:35
# @Email   : 944921374@qq.com
# @File    : demo4.py
# @Description:
import numpy as np
#索引，基础运算
A = np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A))#查看第几位是最小值，不是看值
print(np.mean(A))#输出平均值
print(np.argmax(A))#输出第几位是最大值

print(np.average(A))#也是输出平均值
print(np.median(A))#这是输出中位数
print(np.cumsum(A))#输出累加的和，最终生成一维数组
print(np.diff(A))#输出累差，相差两位数相减
print(np.nonzero(A))#输出不为零的项
print(np.sort(A))#输出排序
print(A.T)#转置，将行变成列
print(A.T.dot(A))
print(np.clip(A,5,9))#所有小于5的数都变成5，大于9的数都变成9，中间的数保持不变
print(np.mean(A,axis=0 ))#输出第一行的平均值
