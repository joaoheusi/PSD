import numpy as np
import matplotlib.pyplot as plt
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

plt.subplot(3, 1, 1)
plt.plot(w, X)

#Hz

F_Hz = (w/ (np.pi)) * (Fs/2)

plt.subplot(3, 1, 2)
plt.plot(F_Hz, X)

#Db

X_Db = 20 * np.log10(X)
plt.subplot(3, 1, 3)
plt.plot(F_Hz, X_Db)

plt.show() 
