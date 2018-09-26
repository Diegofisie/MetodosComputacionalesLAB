import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq
###############################Punto 1#####################################
##############1.1
def y1(t):
	return np.sin(2*np.pi*40*t)
def y2(y):
	return 0.5*np.sin(2*np.pi*90*t)
t = np.linspace(0,0.2,1000)
y = y1(t) + y2(t)
plt.subplot(311)
plt.plot(t,y)
plt.subplot(312)
plt.plot(t,y1(t))
plt.subplot(313)
plt.plot(t,y2(t))
plt.title('Funcion Original')
plt.show()
####################1.2
fourier = fft(y)
frecuencia = fftfreq(len(t))
plt.figure()
plt.plot(frecuencia, abs(fourier))
plt.title('Transformada')
plt.xlim(-0.05,0.05)
plt.show()
###############################Punto 2#################################
####################2.1
data = np.loadtxt("datos_s2.txt", delimiter = " ", skiprows = 1)
data_t = data[:,0]
data_yt = data[:,1]
plt.figure()
plt.plot(data_t,data_yt)
plt.show()
####################2.2
fourier2 = fft(data_yt)
frecuencia2 = fftfreq(len(data_t))
plt.figure()
plt.plot(frecuencia2,abs(fourier2))
plt.title('Tranformada de datos')
plt.xlim(-0.02,0.02)
plt.show()
####################2.3
ffiltro = fourier2*(abs(frecuencia2)<0.016)
f_inf = ffiltro*(abs(frecuencia2)<0.007)
f_sup = ffiltro*(abs(frecuencia2)>0.007)
y_inf = ifft(f_inf)
y_sup = ifft(f_sup)
plt.figure()
plt.subplot(211)
plt.plot(data_t,y_inf,label= 'Corte bajas')
plt.legend()
plt.subplot(212)
plt.plot(data_t,y_sup, label = 'Corte de altas')
plt.legend()
plt.show()
####################2.4
yrec = y_inf + y_sup 
plt.title("Funcion sin ruido y con ruido")
plt.plot(data_t,data_yt, label='Funcion con ruido')
plt.plot(data_t,yrec,label='Funcion limpia', linewidth = 3)
plt.legend(loc = 0)
plt.grid(True)
plt.show()



