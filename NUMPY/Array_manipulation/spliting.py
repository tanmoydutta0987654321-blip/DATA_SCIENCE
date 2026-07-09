import numpy as np
a=np.array([10,20,30,40,50,60])
res=np.split(a,3)
print(res)
b=np.array([10,20,30,40,50])
res=np.array_split(b,3)
print(res)

