
# coding: utf-8

# In[30]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[31]:

##############Punto 1################
def Pol_legendre(x,n):
    return (x**2-1)**n
def fac(n):
    if n == 0:
        return 1
    return n*fac(n-1)


# In[115]:

##############Punto 2################
def f_0(x):
    return 1
def f_1(x):
    return x
def f_2(x):
    return 0.5*(3*x**2 - 1)
x = np.linspace(-1,1,1000)
cer = np.linspace(1,1,1000)
plt.title("Polinomios de Legrende")
plt.plot(x,cer, label = "L_1")
plt.legend(loc = 0)
plt.plot(x,f_1(x),label = "L_2")
plt.legend(loc = 0)
plt.plot(x,f_2(x),label = "L_3")
plt.legend(loc = 0)
plt.ylim(-2,2)
plt.show()



# In[48]:

##############Punto 3################
def primer_polinomio(x):
    return Pol_legendre(x,0)*1/(2**0 * fac(0))
x = np.linspace(-1,1,1000)
plt.plot(x,primer_polinomio(x))
plt.ylim(-2,2)
plt.show()


# In[90]:

##############Punto 4################
#segundo polinomio
def primera_derivada(f):
    n= 10000
    h = x[1]-x[0]
    derivada = (f[1:] - f[0:-1])/h
    primer_poli = derivada*(1./float(fac(1)*2))
    return primer_poli
poli_1 = primera_derivada(Pol_legendre(x,1))
plt.plot(x[0:-1], poli_1)
plt.show()


# In[98]:

##############Punto 5################
#tercer polinomio
def segunda_derivad(f):
    n = 10000
    h = x[1]-x[0]
    derivada_seg = (f[2:-1] -2*f[1:-2] + f[0:-3])/(h**2)
    segundo_poli = derivada_seg*(1./(2**2)*fac(2))
    return segundo_poli
poli_2 = segunda_derivad(Pol_legendre(x,2))
plt.plot(x[1:-2], poli_2)
plt.show()


# In[117]:

##############Punto 6################
plt.plot(x[0:-1], abs(f_0(cer) - poli_1), label = "error poli:0")
plt.legend(loc = 0)
plt.show()


# In[ ]:



