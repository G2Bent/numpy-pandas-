#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/23 14:51
# @Email   : 944921374@qq.com
# @File    : demo1.py
# @Description:
import numpy as np

array = np.array([[1,2,3],[2,3,4]])
#输出array内容
print(array)
#几维数组
print('number of dim:',array.ndim)
#行数是多少,列数是多少
print('shape:',array.shape)
#输入有多少元素
print('size:',array.size)
