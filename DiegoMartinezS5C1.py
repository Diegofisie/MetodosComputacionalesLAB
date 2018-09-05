
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


# In[80]:

def gauss_red(matrix):
    filas = len(matrix)
    col = filas + 1
    for D in range(filas):
        for I in range(D+1, filas):
            if matrix[D][D] != 0:
                break
            matrix[[D,I]] = matrix[[I,D]]
            if matrix[D,D] != 0.0:
                matrix[D] = matrix[D]/float(matrix[D,D])
        for E in range(filas):
            if E != D:
                matrix[E] = matrix[E]-matrix[D]*matrix[E,D]
    G = matrix
    return G
            


# In[84]:

matrix = np.array([[1,2,2,7],[1,2,3,8],[1,1,1,9]])
print gauss_red(matrix)


# In[ ]:




# In[ ]:



