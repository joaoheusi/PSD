import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp
plt.style.use('seaborn')
np.seterr(divide='ignore', invalid='ignore')

FS = 8000
W = np.arange(np.pi / 1000, np.pi, np.pi / 1000)

passo = np.pi/ 1000

#Variáveis
w = np.arange(0,np.pi,passo)
L = 8
Fs = 8000

#Numerador e Denominador
num = np.sin((w*L)/2)
den = np.sin(w/2)

#Equacao Base

temp = (num/den)

#Rad

X = (1/L) * (abs(temp))

plt.subplot(4, 1, 1)
plt.xlabel('Frequencia')
plt.title('Frequencia em Hz')
plt.plot(w, X)



#Hz

F_Hz = (w/ (np.pi)) * (Fs/2)

plt.subplot(4, 1, 2)
plt.title('Frequencia em Hz')
plt.xlabel('Frequencia')
plt.plot(F_Hz, X)

#Db

X_Db = 20 * np.log10(X)
plt.subplot(4, 1, 3)
plt.title('Frequencia em Hz')
plt.ylabel('Atenuacao DB')
plt.xlabel('Frequencia')
plt.plot(F_Hz, X_Db)


#Usando Freqz para obter a resposta em frequencia
# num = [ 0.25, 0.25, 0.25, 0.25]
num = [ 0.1, 0.2, 0.4 ,0.2 , 0.1]
den = 1

f, h = sp.freqz(num,den,fs=Fs)
plt.subplot(4, 1, 4)
plt.title('Magnitude da resposta em frequencia')
plt.plot(f*Fs/(2*np.pi), 20*np.log10(abs(h)))
plt.tight_layout(pad=1.0)
plt.show() 
