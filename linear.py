from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
a1=3
a2=4
x1=[1,2,3,4,5]
x2=[2,4,6,8,2]
y1=[]
y2=[]
j=cmath.sqrt(-1)
n=8
for n in range(0,(len(x)-1)):
	sum=0
	for k in range(0,(len(x)-1)):
		sum=sum+(x1[n]*np.exp(-j*3.14*2*n*k)/N)
    y.append(sum)
for n in range(0,(len(x)-1)):
	sum1=0
	for k in range(0,(len(x)-1)):
		sum1=sum1+(x2[n]*np.exp(-j*3.14*2*n*k)/N)
    y.append(sum1)
if(a1*x1[k]+a2*x2[k])=(a1*x1[k]+a2*x2[k]):
	print("linearity property exist")
else:
	print("linearity property does not exist")
