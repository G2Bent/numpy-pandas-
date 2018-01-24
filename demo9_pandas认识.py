#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 9:30
# @Email   : 944921374@qq.com
# @File    : demo9.py
# @Description:这节开始讲pandas，更像是一种字典型的numpy
import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,44,1])
print(s)
A = pd.Series([np.arange(12).reshape(3,4)])
print(A)
#按日期索引排序
dates = pd.date_range('20180124',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20180124'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print(df2)
#每一维的数据类型
print(df2.dtypes)
#打印列序号
print(df2.index)
#打印横的序号
print(df2.columns)
#打印里面的值
print(df2.values)
#描述基本运算，只能描述整数
print(df2.describe())
#转置，横向和纵向对换
print(df2.T)
#倒排序
print(df2.sort_index(axis=1,ascending=False))
#对值进行排序
print(df2.sort_values(by='E',ascending=False))