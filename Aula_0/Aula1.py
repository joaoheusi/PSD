import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

#Carregar dados
spf = open('alo.pcm', 'rb')
pcmdata = spf.read()

#De buffer para Array np.int16
a = np.frombuffer(pcmdata,np.int16)

#Array x do comprimento do array lido
x = np.arange(len(a))

#Plotar gráfico do áudio original
plt.figure( figsize=(20,6))
plt.plot(x, a)
plt.show()

#transformar array
new_y = a * 0.5

#Plotar gráfico do áudio transformado
plt.figure( figsize=(20,6))
plt.plot(x, new_y)
plt.show()

#salvar em um novo arquivo o áudio transformado.
saida_file = open('saida_alo.pcm', 'wb')
scaled = np.int16(new_y)
saida_file.write(scaled.tobytes())
saida_file.close()
