import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp
plt.style.use('seaborn')
np.seterr(divide='ignore', invalid='ignore')

pi = np.pi
W0 = 2*pi*1000

f0 = W0/(2*pi)


num = [0, W0 ]
den = [0, W0 ]

H = sp.TransferFunction(num, den)

sp.bode(H)

Fs = 8000
Ts = 1/Fs

Hd = sp.cont2discrete(H,Ts,method='tustin')

w, h = sp.freqz(num[0],den[0])
figure(2)
plot(w*Fs/(2*pi), 20*np.log10(abs(h)))
plt.show()