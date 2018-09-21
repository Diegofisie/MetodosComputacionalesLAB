import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
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
filtrado = fourier[np.where(abs(f)>1/7.0)]=0
datos_filtrados = ifft(fitrado)

