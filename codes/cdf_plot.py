#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def uni_cdf(x):
    if(x < 0):
        return(0)
    elif(x > 1):
        return(1)
    else:
        return(x)

vec_uni_cdf = np.vectorize(uni_cdf, otypes=[float])
uni_val = vec_uni_cdf(x)
plt.plot(x.T, uni_val,'o-')

plt.plot(x.T,err,'bo')#plotting the CDF
plt.grid() #creating the grid
plt.legend(["Theory","Numerical"])
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
plt.savefig('../figs/uni_cdf.pdf')
plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#else
#plt.show() #opening the plot window
