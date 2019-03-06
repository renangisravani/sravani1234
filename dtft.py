import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dtft(x):
    
   
    j=cm.sqrt(-1)
    y=[]
    n=len(x)
    N=10000
    q=np.linspace(0,2*np.pi,N)
    for i in range(0,N):
	w_1=q[i]
	sum=0
     for k in range(0,n):
            sum=sum+(x[k]*np.exp(-k*w_1*j))
     y.append(abs(sum))
       
     return y
x=input("enter x values")
t=dtft(x)
plt.plot(t)
plt.show()
  
