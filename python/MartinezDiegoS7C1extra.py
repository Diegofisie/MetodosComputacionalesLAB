
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt


# In[9]:


def fun_cos(x):
    return np.cos(x**2)


# In[17]:


def transformada_fouier(x,k,n):
    sumatoria = 0
    for i in range(n):
        sumatoria = sumatoria + x[i]*np.exp((-2*np.pi*1j*i*k)/float(n))
    return sumatoria
N_puntos = 100
x = fun_cos(np.linspace(0,6,N_puntos))
k = np.linspace(0,N_puntos,N_puntos)
y = transformada_fouier(x,k,N_puntos)
plt.scatter(k,abs(y))
f = np.fft.fftfreq(N_puntos,6.0/N_puntos)
plt.show()
plt.close()
plt.scatter(f,abs(y))
plt.show()

