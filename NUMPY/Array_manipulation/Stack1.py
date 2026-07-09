import numpy as np
#Normal stack
a=np.array([10,20,30])
b=np.array([4,5,6])
c=np.stack((b,a))
print(c)
#It is normal stack
a=np.array([6,7,8])
B=np.array([1,2,3])
res=np.stack((a,B))
print(res)
#It is hstack
a=np.array([6,7,8])
B=np.array([1,2,3])
res=np.hstack((a,B))
print(res)
#It is vstack
a=np.array([6,7,8])
B=np.array([1,2,3])
res=np.vstack((a,B))
print(res)
