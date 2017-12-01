'''
Created on 2017. 11. 19.

@author: jihye
'''

import numpy as np
a=np.array([[1,2,3,1],[4,2,3,2],[1,9,2,3]])
b=np.sort(a)
c=np.sort(a,axis=0)
print(b)
print(c)
