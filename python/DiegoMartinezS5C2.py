
# coding: utf-8

# In[27]:

from numpy import *
import numpy as np


# In[ ]:




# In[51]:

def fulladder(m1,m2):
    suma = (m1+m2)
    ppunto = np.dot(m1,m2)
    inversa_b = np.linalg.inv(m2)
    transpuesta_a = np.matrix.transpose(m1)
    eig_valores,eig_vectores = np.linalg.eig(m2)
    return suma,ppunto,transpuesta_a,inversa_b, str("los valores propios de B son:"),eig_valores,str("los vectores propios son:"), eig_vectores


# In[53]:

a = np.array([[1,2,5],[5,6,7],[8,9,10]])
b = np.array([[2,2,5],[4,5,7],[8,9,8]])
fulladder(a,a)


# In[72]:

def sis_ecuaciones(m,v):
    filas_m, colum_m = m.shape
    len_v = len(v)
    if filas_m == len_v:
        solucion = np.linalg.solve(m,v)
    return solucion


# In[79]:

a = np.array([[1,2,5],[5,6,7],[8,9,10]])
b = np.array([1,2,3])
sis_ecuaciones(a,b)


# In[ ]:




# In[ ]:



