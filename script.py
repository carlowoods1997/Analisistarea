import numpy as np
import matplotlib.pyplot as plt

#Definición de la señal en el dominio del tiempo
fs = 1000  # Frecuencia de muestreo
t = np.arange(0, 1, 1/fs)  # Vector de tiempo (1 segundo)
f_seno = 5  # Frecuencia de la señal (5 Hz)
senal = np.sin(2 * np.pi * f_seno * t)

#Cálculo de la Transformada de Fourier
n = len(senal)
fourier = np.fft.fft(senal)
frecuencias = np.fft.fftfreq(n, 1/fs)

#Normalización y magnitud
magnitud = np.abs(fourier) / n

#Visualización de los resultados
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, senal)
plt.title('Señal en el dominio del tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.subplot(2, 1, 2)
plt.plot(frecuencias[:n//2], magnitud[:n//2])
plt.title('Espectro de frecuencia (Transformada de Fourier)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')

plt.tight_layout()
plt.show()