# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UXiYtOYFBUjvAV6RzjRm-ffO66Qx7_w8
"""

import pandas as pd
import numpy as np

m=np.random.randint(3,30,size=(10,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])

df

"""loc : tanımlandığı şekli ile seçim yapmak için kullanılır."""

df.loc[0:3]

"""iloc:alışık olduğumuz indexleme mantığı ile seçim yapar."""

df.iloc[0:3]

df.loc[0:3,"var2"]

df.var1

df[df.var1>15]["var1"]

df[(df.var1>15)&(df.var3>=19)]

m1=np.random.randint(3,30,size=(10,3))
df1=pd.DataFrame(m1,columns=["var1","var2","var3"])

df1

df2