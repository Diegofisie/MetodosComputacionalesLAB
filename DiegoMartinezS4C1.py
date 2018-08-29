import numpy as np
import matplotlib.pyplot as plt
#f es la funcion
#x es el vector, el linspace 
#h es el intervalo h 
#n es el numero de pasos
#-----------------------------------------------------------------------------------------------#
def derivada(f,x,h, metodo = ""):
    if metodo == "FD":
        return (f(x+h) - f(x))/h
    if metodo == "CD":
        return (f(x+h/2) - f(x-h/2))/h
    if metodo == "EP":
        return (8.0*(f(x+h/4.0)-f(x-h/4.0))-(f(x+h/2.0) - f(x-h/2.0)))/3/h
    else:
        return "Systax error"
def mi_fun(x):
    return np.cos(x)**2
def mi_fun_prim(x):
    return -2*np.sin(x)*np.cos(x)
n = 10000
x = np.linspace(1.0,1.0,n)
h = np.linspace(10**(-2), 10**(-10),n)
print h

derivada_analitica = mi_fun_prim(x)### analitica
FD = derivada(mi_fun,x,h,"FD")### numerica
CD = derivada(mi_fun,x,h,"CD")### numerica
EP = derivada(mi_fun,x,h,"EP")### numerica
errorFD = (FD - derivada_analitica)/derivada_analitica
errorCD = (CD - derivada_analitica)/derivada_analitica
errorEP = (EP - derivada_analitica)/derivada_analitica

plt.subplot(311)
plt.plot(h,abs(errorFD),label="Error FD")
plt.legend(loc = 0)
plt.subplot(312)
plt.plot(h,abs(errorCD),label="Error CD")
plt.legend(loc = 0)
plt.subplot(313)
plt.plot(h,abs(errorEP),label="Error EP")
plt.legend(loc = 0)
plt.show()


	
	

