
# coding: utf-8

# In[96]:


import numpy as np
import matplotlib.pyplot as plt


# In[97]:


datos = np.loadtxt("647_Global_Temperature_Data_File.txt")
datos.shape


# In[98]:


años = datos[:,0]
anomalias = datos[:,1]
anomalias_suavizadas = datos[:,2]


# In[99]:


plt.title("anomalías en función de los años")
anomaliasplot = plt.plot(años,anomalias, label = "Anomalías en función de los años")
plt.legend(loc = 0)
plt.grid(True)
plt.savefig('Grafica_temp.pdf',format="pdf")


# In[100]:


ajuste = np.where(datos[:,1] > 0.5)
años_tem = datos[ajuste,0]
print("Los años en los cuales las anomalías fueron mayoes a 0.5 son:", años_tem)


# In[101]:


#Un año mas caliente significa una anomalía mas alta
anomalias =datos[:,1]
frio_a_calido= sorted(anomalias, reverse = True)
mas_calientes = sorted(frio_a_calido[0:20])
print(mas_calientes)


# In[106]:


plt.title("anomalías Suavizadas en función de los años")
anomaliasplot = plt.plot(años,anomalias_suavizadas, label = "Anomalías suavizadas en función de los años")
plt.legend(loc = 0)
plt.grid(True)
plt.savefig('Grafica_temp2.pdf',format="pdf")

