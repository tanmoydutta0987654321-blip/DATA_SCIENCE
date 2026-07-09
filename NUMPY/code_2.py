import numpy as np
a=np.array([123,127,128],dtype="<U2")
a=a.astype(np.bool_)
print(a)
print(a.dtype)
print(f"{a.nbytes} bytes")
