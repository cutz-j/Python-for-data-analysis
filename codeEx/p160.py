# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 14:24:36 2018

@author: 403-10
"""

from pandas import Series, DataFrame

aSeries=Series([1,2,3,"a"])
bSeries=Series([4,5,6,"b"])
print(aSeries+bSeries)
sumSeries=aSeries+bSeries
sumSeries.name="sum"
sumSeries.index.name="category"
print(sumSeries)

aDict={'a':[1,2,3,4,5], 'b':[1,2,3,5,6], 'c':[34,5,6,6,1]}
aDf=DataFrame(aDict, columns=["a","b","c"])
print(aDf)
print(aDf["a"])
aDf.a=15
print(aDf)
aDf.a=aSeries
print(aDf)

obj3=Series(['blue','purple','yellow'], index=[0, 2, 4])
print(obj3)
obj3=obj3.reindex([0,1,2,3,4,5], method='pad')