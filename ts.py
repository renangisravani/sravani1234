from scipy import signal
import cmath
import numpy as np
import matplotlib.pyplot as plt
x=[1,2,4,5]
j=cmath.sqrt(-1)
print(x)
N=4
y=[]
for n in range(0,len(x)-1):
    sum=0
    for k in range(0,(len(x)-1)):
        sum=sum+(x[n]*np.exp(-j*3.14*2*n*k)/N)
    y.append(sum)
print(y[k])
s=len(x)
print("s\n",s)
l=2
y[len(x)-l]=[]
if(y[k]==y[len(x)-l]):
	print("the time shifting property exist")
else:
	print("the time shifting property does not exist")

