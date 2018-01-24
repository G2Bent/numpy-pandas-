#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 11:54
# @Email   : 944921374@qq.com
# @File    : demo15.py
# @Description:merge 合并
import pandas as pd
import numpy as np

#merging two df by key/keys(may be used in database)
#simple example
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})

print(left)
print(right)
res = pd.merge(left,right,on = 'key')
print(res)


#consider two keys
left = pd.DataFrame({'key0':['K0','K0','K2','K3'],
                     'key1':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key0':['K0','K1','K2','K3'],
                      'key1':['K0','K1','K0','K3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})
print(left)
print(right)
#how = ['left','right','inner','outer']
res = pd.merge(left,right,on = ['key0','key1'],how = 'left')
print(res)


#indicator 默认情况输出的值为_merge，如果需要修改的话，直接在传入参数改就可以了
df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,3],'col_right':[2,2,2]})
print(df1)
print(df2)

res = pd.merge(df1,df2,on = 'col1',how = 'outer',indicator=True)
res2 = pd.merge(df1,df2,on = 'col1',how='outer',indicator="indicator_ca")
print(res)
print(res2)

#merge by index
left = pd.DataFrame({'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']},
                     index=['K0', 'K0', 'K2', 'K3'],)
right = pd.DataFrame({'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']},
                        index=['K0','K1','K2','K3'],)
print(left)
print(right)
#left_index and right_index
res = pd.merge(left,right,left_index=True,right_index=True,how = 'outer')
print(res)

#handle overlapping将相同的两个age分开识别
boys = pd.DataFrame({'k':['K0','K1','K2','K3'],'age':[1,2,3,4]})
girls = pd.DataFrame({'k':['K0','K1','K2','K3'],'age':[3,4,5,6]})
res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how = 'inner')
print(res)

