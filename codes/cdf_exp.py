#Importing numpy, scipy, mpmath and pyplot
from cmath import log
import numpy as np
import math
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
randvar = -2*np.log(1-randvar)
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def log_cdf(x):
    if(x < 0):
        return(0)
    else:
        return(1 - math.exp(-x/2))

vec_log_cdf = np.vectorize(log_cdf, otypes=[float])
log_val = vec_log_cdf(x)
	
plt.plot(x.T,log_val)
plt.plot(x.T,err,'bo')#plotting the CDF
plt.grid() #creating the grid
plt.legend(["Theory","Numerical"])
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
plt.savefig('../figs/exp_cdf.pdf')
plt.savefig('../figs/exp_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#else
#plt.show() #opening the plot window
