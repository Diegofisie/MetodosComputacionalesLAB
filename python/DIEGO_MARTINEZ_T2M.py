import numpy as np
import matplotlib.pyplot as plt
############################################Punto 1,2,3################################
class punto:
	def __init__(self,x = 0,y = 0):
 	    self.x = x
	    self.y = y
	    self.r = np.sqrt((x**2+y**2))
	def move(self,x,y):
	    self.x = self.x + x
	    self.y = self.y + y
	    self.r = np.sqrt((self.x**2+self.y**2))
	def pozixion(self):
	    print(self.x,self.y,self.r)
############################################Punto 4################################ 
archivo = open("caminata.txt","w")
############################################Punto 5################################
variabledelpunto = punto()
i = 0
while variabledelpunto.r <= 10:
	variabledelpunto.move(np.random.rand()*2-1,np.random.rand()*2-1)
	i = i +1
############################################Punto 6################################
pasos = punto()
pos = []
def ptlc(Nsimu,Npasos):
	for i in range(Nsimu):
	    for j in range(Npasos):
	    	pasos.move(np.random.rand()*2-1,np.random.rand()*2-1)
	    archivo = open("caminata.txt","w")
	    escribe = pasos.r,"Simulaci`on",j
 	    archivo.write(str(escribe))
	    archivo.close()
	    pos.append(pasos.r)
	return pos
print ptlc(50,100)
print ptlc(100,100)
print ptlc(1000,50) # ---> Por el teorema del limite central entre mas N hayan mejor ser`a 
############################################Punto 7###############################

plt.hist(ptlc(1000,50),bins = 50)
plt.show()



		
		
	





