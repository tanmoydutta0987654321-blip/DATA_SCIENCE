import numpy as np
array=np.array('A')#ZERO DIMENSIONAL ARRAY
print(array.ndim)
array=np.array(['T','A','N','M','O','Y'])#ONE DIMENSIONAL ARRAY
print(array.ndim)
array=np.array([['T','A','N','M','O','Y'],
                ['D','U','T','T','A']]) #TWO DIMENSIONAL ARRAY
print(array.ndim)
array=np.array()
