# numpy ndarray
import numpy as np

data=np.random.randn(2,3)

data1=[6,7.5,8,0,1]
arr1=np.array(data1)
print(arr1)
# array= 다차원 동일자료형

np.arange(15)
arrayList=np.arange(10)
numList=[]
for i in range(0,10):
    numList.append(i)

numList[5:8]
arrayList[5:8]=12
print(numList,"\n",arrayList)

# array[0][2] == array[0,2] 위치접근

names=np.array(["B","J","W","B","W","J","J"])
data=np.random.rand(7,4)