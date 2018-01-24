#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 9:52
# @Email   : 944921374@qq.com
# @File    : demo10.py
# @Description:选择数据
import pandas as pd
import numpy as np

dates = pd.date_range('20180124',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df['A'],df.A)
print(df[0:3],df['20180125':'20180126'])
#使用select by label:loc
print(df.loc['20180126'])
print(df.loc[:,['A','B']])

#select by position:iloc
#切割
print(df.iloc[3:5,1:3])

#select by selection:ix合并筛选
print(df.ix[:3])

#Boolean indexing筛选大于或小于数列
print(df[df.A>8])



