
# coding: utf-8

# In[60]:

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp
import numpy.linalg as npl
get_ipython().magic(u'pylab inline')


# In[61]:

########################### Punto 1##########################################################
check = 5.0 #puntos
########################### Punto 2##########################################################
hamiltoniano = np.array([[0,0,0,0],[0,-2.0,1.0,0],[0,1.0,-2.0,0],[0,0,0,-4.0]])
hamiltoniano


# In[62]:

########################### Punto 3##########################################################
T = 1
N = 10000.0
t = T/N
U = sp.expm(hamiltoniano*-1j*t) 


# In[63]:

########################### Punto 4##########################################################
unosbreraizdedos = 1/np.sqrt(2)
x_vec = unosbreraizdedos*np.array([[0],[1],[1],[0]])
x_vec


# In[69]:

########################### Punto 5##########################################################
A = np.linalg.matrix_power(U,int(N))
x_0 = np.linalg.solve(A,x_vec)
x_0


# In[72]:

########################### Punto 6##########################################################
sol =np.matmul(A,x_0)
sol


# In[ ]:




# In[ ]:




# In[ ]:



