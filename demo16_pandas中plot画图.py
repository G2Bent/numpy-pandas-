#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 13:49
# @Email   : 944921374@qq.com
# @File    : demo16.py
# @Description:pandas 图表
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot生成图表


#Series线性数据
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data_add = data.cumsum()
data_add.plot()
plt.show()

#DataFrame
data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
data = data.cumsum()
print(data.head())
#plot methods：
#'bar'：条形图；
# 'hist',
# 'box',
# 'kde',
# 'area',
# 'scatter':点图,
# 'hexbin',
# 'pie'
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label = 'Class 1')
bx = data.plot.scatter(x='C',y='D',color='Pink',label = 'Class 3')
data.plot.scatter(x='A',y='C',color='Green',label = 'Class 2',ax = bx)
# data.plot()
plt.show()
