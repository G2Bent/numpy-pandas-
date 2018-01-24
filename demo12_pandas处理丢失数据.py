#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 10:21
# @Email   : 944921374@qq.com
# @File    : demo12.py
# @Description:pandas处理丢失数据
import pandas as pd
import numpy as np

dates = pd.date_range('20180124',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)
df.iloc[2,2] = np.nan
df.iloc[0,2] = np.nan
print(df)
#将nan的值数据都丢掉，默认丢掉横
print(df.dropna(axis=0,how='any'))

#将nan的数据给填上
print(df.fillna(value = 0))

#检查里面到底是不是有数据
print(np.any(df.isnull()) == True)

