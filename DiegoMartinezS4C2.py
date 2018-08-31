
# coding: utf-8

# In[100]:

import numpy as np
import matplotlib.pyplot as plt


# #### Escriba un programa que encentre los ceros de f(x) en un intervalo dado 

# In[101]:

a = 0.5
def mi_func(x):
    return np.sin(x)*np.exp(-a*x)

def mi_func_prime(x):
    h = 0.0001
    return (mi_func(x+h) - mi_func(x-h))/(2*h)


# #### Newton Raphson

# In[150]:

def newton(x,n,e):
    while np.abs(mi_func(x))>e:
        for i in range(n,error):
            if mi_func_prime == 0:
                x = x + np.pi/1000
            else:
                x = x - mi_func(x)/mi_func_prime(x)
        return x


# In[157]:

def ceros(errores,a,b,e):
    errores = []
    x = a
    while x < b:
        primer_cero = newton(x,n,e) 
        if primer_cero < a or primer_cero > b:
            x = x + 0.01
        else:
            errores.append(primer_cero)
            ceros(errores,error,1.0,primer_cero-np.pi-0.02)            


# In[158]:

def error_entre_intervalo(errores,a,error):
    for i in eerores:
        if np.abs(i-a) < error:
            return True
    return False
print newton(5.0,10,0.01)
ceros(errores,error,1,0.001)
print errores


# In[ ]:




# In[ ]:



