# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XSN9RPP1C6wFnOyftb1mXyVMQthXh6mB
"""

import numpy as np

"""Array birleştirme"""

x=(np.array([1,2,3]))
y=(np.array([4,5,6]))

np.concatenate([x,y])

a=np.array([[1,2,3],
         [4,5,6]])

np.concatenate([a,a])

np.concatenate([a,a],axis=0)

np.concatenate([a,a],axis=1)

m=np.random.normal(20,5,(3,3))

"""satır sıralama axis=1"""

np.sort(m,axis=1)

np.sort(m,axis=0)

"""index ile elemanlara erişme"""

a=np.random.randint(10,size=10)

a

a[0]

m=np.random.randint(10,size=(3,5))
m

m[0,1]

a[0:3]

a[3:]

a[0::3]

a[2::2]

"""2. indexten başlar 2 şer index atlayarak verileri getirir.

2 boyutlu arraylerde slice işlemleri
"""

n=np.random.randint(10,size=(5,5))
n

n[:,0]

"""n arrayin 1. sütununu getirir."""

n[0,:]

"""n arrayinin 1.satırını getir."""

n[0:2,0:3]

"""0 dan 2ye satırları 0 dan 3 sütunları alır."""

n

alt_a=n[0:3,0:2]
alt_a

"""oluşturduğumuz alt array de değişiklik yaptığımızda ana array de bundan etkilenir."""

alt_a[0,0]=9999
alt_a[1,1]=8899

alt_a

n

alt_c=n[0:3,0:2].copy()
alt_c

alt_c[0,1]=11111
alt_c

n

"""sonuna copy ekleyince ana array etkilenmez"""

v=np.arange(0,30,3)
v

v[3]

"""fancy index ile erişmek"""

alt_getir=[1,3,5]
v[alt_getir]

b=np.arange(9).reshape(3,3)
b

satir=np.array([0,1])
sütun=np.array([1,2])

b[satir,sütun]

b

c=np.arange(1,20,2)
c

c>11

c[c>11]

c*2

c/5

c-1

c*5/10-1

np.subtract(c,1)

c

np.add(c,1)

np.multiply(c,3)

np.divide(c,3)

c**2

c**3

np.power(c,3)

c%2

np.mod(c,2)

np.absolute(np.array([-3]))

"""mutlak değer fonksiyonu"""

np.sin(0)

np.cos(45)

np.log2(v)

np.log10(v)

"""iki bilinmeyenli denklem çözümü

5*x0+x1=12

x0+3*x1=10
"""

a=np.array([[5,1],[1,3]])
b=np.array([12,10])

a

b

x=np.linalg.solve(a,b)
x