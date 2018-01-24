#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 10:06
# @Email   : 944921374@qq.com
# @File    : demo11.py
# @Description:
import pandas as pd
import numpy as np

dates = pd.date_range('20180124',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)
df.iloc[2,2] = 1111
print(df)
df.loc['20180125','B'] = 123
print(df)
df.B[df.A>4] = 0
print(df)
df['F'] = np.nan
print(df)
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20180126',periods=6))
print(df)