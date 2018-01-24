#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/24 10:27
# @Email   : 944921374@qq.com
# @File    : demo13.py
# @Description:导入导出数据
import pandas as pd
import numpy as np
import os
import sys
file_path = os.getcwd()+'\student.csv'
print(file_path)
#python3.6改了文件输入输出系统的默认编码，从"mbcs" 改为"UTF-8"
sys1 = sys.getfilesystemencoding()#查看修改前的编码
print(sys1)
sys._enablelegacywindowsfsencoding()#进行修改
sys2 = sys.getfilesystemencoding()#查看修改后的编码
print(sys2)
data = pd.read_csv(file_path)
print(data)


