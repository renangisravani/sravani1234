import numpy as np
import matplotlib.pyplot as mp
import cmath 
j=cmath.sqrt(-1)
N=4
x=[1,2,3,4]
n=len(x)
y=[ ]
for i in range(0,n):
             sum=0
             for k in range(0,n-1,1):
                   sum=sum+(x[k]*np.exp(-j*2*np.pi*k*i/N))
             y=np.append(y,sum)
print (y)
mp.plot(y)
mp.show()
