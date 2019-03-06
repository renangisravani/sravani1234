import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('song.wav')
print(fs)
plt.plot(data,'r')
plt.xlabel('samples')
plt.ylabel('wave')
plt.show()
wav.write('jaya.wav',(4)*fs,data)