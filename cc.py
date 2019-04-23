from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4]
N=8
y=[]
j=cmath.sqrt(-1)
for n in range(0,(len(x)-1)):
        sum=0
        for k in range(0,len(x)-1):
               sum=sum+(x[n]*np.exp(-j*2*3.14*k*n)/N)
        y.append(sum)
x1=[1,2,3,4,5]
N=8
y1=[]
j=cmath.sqrt(-1)
for n in range(0,len(x1)-1):
      sum1=0
      for k in range(0,(len(x)-1)):
             sum1=sum1+(x1[n]*np.exp(-j*2*3.14*k*n)/N)
      y.append(sum1)
y3=[]
y3=y1[k]*y[k]
if(y1[k]*y[k]==y3):
	print("circular convolution exist")
else:
	print("circular convolution does not exist")
