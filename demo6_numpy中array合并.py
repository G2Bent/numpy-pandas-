#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/23 17:04
# @Email   : 944921374@qq.com
# @File    : demo6.py
# @Description: numpy array合并
import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])
C = np.array([3,3,3])
D = np.vstack((A,B,C))#将两个数组合并起来
print(A.shape,C.shape)
E = np.hstack((A,B))
print(E)#左右合并
print(A.shape,E.shape)
print(A[:,np.newaxis])
G = np.hstack((A[:,np.newaxis],B[:,np.newaxis]))
print(G)

H = np.concatenate((A,B,B,A))#也是进行合并，也可以使用axis来进行纵横合并
print(H)
