import numpy as np
import matplotlib.pyplot as plt
import sys 
#from sympy import *
import scipy.integrate as sp
#-------------------------Punto 1-------------------------------------------##
N = sys.argv[1]
Np = sys.argv[2]
def poli(x):
    return (35*x**4.0 - 30*x**2.0 + 3.0)/8.0
x = np.linspace(-1.0,1.0,int(float(N)))
pol = poli(x)
plt.plot(x,pol, label = "Funcion original")
plt.legend(loc = 0)
plt.show()
#-------------------------Punto 2-------------------------------------------##
#--------------------------Punto 3-- Sympy no funciona :c-------------------##
####j = Symbol('j')
####def integ(x):
####    return integrate((35*j**4.0 - 30*j**2.0 + 3.0)/8.0 , j)
####valor = integ(x)
valor = 0
print valor
#--------------------------Punto 4--------------------------------------------##
def rampa(x):
    return x*(x>=0)
plt.plot(x,rampa(poli(x)))
plt.plot(x,-rampa(-poli(x)))
plt.show()
#--------------------------Punto 5--------------------------------------------##
random_xpositivo = np.random.rand(int(float(Np)))*2-1
random_ypositivo = np.random.rand(int(float(Np)))
random_xnegativo = np.random.rand(int(float(Np)))*2-1
random_ynegativo= np.random.rand(int(float(Np)))*-1

deltapos = rampa(poli(random_xpositivo)) - random_ypositivo
deltaneg = -rampa(-poli(random_xnegativo)) - random_ynegativo
below  = np.where(deltapos>0.0)
above = np.where(deltaneg<0.0)
plt.scatter(random_xpositivo[below],random_ypositivo[below])
plt.scatter(random_xnegativo[above],random_ynegativo[above])
plt.show()
#--------------------------Punto 6--------------------------------------------##
valor_pos = 2*np.size(below)/float(Np)
valor_neg = 2*np.size(above)/float(Np)
valor_integra = valor_pos - valor_neg
print "El valor de la intergal es:",valor_integra
print "El valor analitico de la integral es:", valor
print "El valor del error del metodo es:", abs(valor_integra - valor)*100 ,"%"
#--------------------------Punto 7--------------------------------------------##
integral_quad = int(sp.quad(poli,-1,1))
print "la integral por quad es:", integral_quad

