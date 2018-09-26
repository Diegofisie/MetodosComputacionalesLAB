import numpy as np 
import matplotlib.pyplot as plt

integralnumerica = (1.0/3.0)
def trapecieitor10mil(funcion,x,y,error):
	n = 100
	valorintegral = 0
	while abs(valorintegral-integralnumerica) > error:
		valorintegral = 0
		delta = float(x-y)/(n)
		for i in range(n+1):
			valorintegral = valorintegral + delta*float(funcion(x+delta*i))/2.0
		else:
			valorintegral = delta + delta*(funcion(x+float(delta*i)))
		if (abs(valorintegral+delta+(funcion(x+delta*i))/2.0) - integralnumerica<error):
			valorintegral = valorintegral + delta*(x+float(delta*i))/2.0
			return valorintegral
def funcion(x):
	return x**2
print trapecieitor10mil(funcion,0,1,0.1)

	

	
