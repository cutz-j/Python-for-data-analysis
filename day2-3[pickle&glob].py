import pickle
f=open("sleep.txt","wb") #write, binary
data={1:"big", 2:"data"}
pickle.dump(data, f)
f.close()

f=open("sleep.txt","rb")
print(pickle.load(f))

# glob
import glob
print(glob.glob("d*"))

# 난수생성기
import random
print(random.random())

# Q1



    