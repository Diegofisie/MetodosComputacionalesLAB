
# coding: utf-8

# In[34]:

import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt
from numpy.linalg import *
from scipy.linalg import expm,inv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[35]:

#Punto 2 
N=1000
x=uniform(0,9,N)
ruido=uniform(-2,2,N)#+np.sin(x1)
y=x+ruido*np.exp(-0.1*(x-5)**2)
z=x+y+uniform(-3,3,N)*np.exp(0.05*(-(x-np.mean(x))**2-(y-np.mean(y))**2))


# In[36]:

#Punto 3
x = x-np.mean(x)
y = y-np.mean(y)
z = z-np.mean(z)
x = x/np.sqrt(np.var(x))
y = y/np.sqrt(np.var(y))
z = z/np.sqrt(np.var(z))
datos=[x,y,z]
print("Las medias son:", np.mean(x),np.mean(y),np.mean(z),"Las varianzas son:",np.var(x),np.var(y),np.var(z))


# In[55]:

#Punto 4
cov = np.cov([x,y,z])
print(cov)


# In[62]:

#Punto 5
val,vec = np.linalg.eig(cov)
vec = np.transpose(vec)
#print("los valores propios de la matriz de covarianza son:" ,val)
#print("Los vectores propios de la matriz de covarianza son:", vec)
principales = vec[0],vec[1]
print("Los componentes principales son:",principales)


# In[63]:

#Punto 6
datos = [x,y,z]
datos_1 = np.matmul(np.transpose(datos),vec[0])
datos_2 = np.matmul(np.transpose(datos),vec[1])
plt.scatter(datos_1,datos_2)
plt.show()


# In[68]:

#Bono
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.scatter(x,y,z)
plt.show()


# In[ ]:




# In[ ]:



