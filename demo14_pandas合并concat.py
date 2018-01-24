#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 11:28
# @Email   : 944921374@qq.com
# @File    : demo14.py
# @Description:pandas 合并concat
import pandas as pd
import numpy as np

#cancatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
res = pd.concat([df1,df2,df3],axis=0)
print(res)
#如果要忽略前面的index，重新排序
res1 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res1)

#join,['inner','outer']
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)

#inner会将各自没有的裁剪掉，默认情况是outer输出
res = pd.concat([df1,df2],join='inner',ignore_index=True)
print(res)

#join_axes
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res = pd.concat([df1,df2],axis=1,join_axes=[df1.index])
print(res)

#append
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['b','c','d','e'],index=[2,3,4])
res = df1.append([df2,df3],ignore_index=True)

print(res)
s1 =pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1.append(s1,ignore_index=True)
print(res)

