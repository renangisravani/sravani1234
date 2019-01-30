import matplotlib.pyplot as plt
import numpy as np
fs=float(input("enter frequency:"))
n=int(input("enter number of samples:"))
x=np.arange(n)
a=np.sin(2*np.pi*fs*x)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show()

