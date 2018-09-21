import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
import numpy.linalg as lag
#Importar los datos txt
datos = np.loadtxt('trm.txt',delimiter = ',')
fourier = fft(datos[:,1])/len(datos)
#Normalizar las fecuencias
dt = 1/365.0
freq = fftfreq(len(datos),dt)
mayor_0 = np.where(freq > 0)
plt.semilogx(freq[mayor_0],fourier[mayor_0] )
plt.show()
plt.savefig("FFT-trm.pdf",format="pdf")
plt.close()
#parte 2
filtro = fourier(abs(freq)<1.0/7.0)
datosfiltrados = ifft(filtro)
diaas = datos[:,0]
anios_ultimos = np.where(diaas>=365*3)
plt.plot(diaas[anios_ultimos], datosfiltrados[anios_ultimos])
plt.plt.savefig("trm 3years limpio.pdf",format="pdf")
