#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import math
import scipy 
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


maxrange=30
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def gau_cdf(x):
    return((1/2) * (1 + math.erf(x/math.sqrt(2))))

vec_gau_cdf = np.vectorize(gau_cdf, otypes=[float])
gau_val = vec_gau_cdf(x)

plt.plot(x,gau_val,'bo')
plt.plot(x,err,'g-')
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])

#if using termux
#plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
plt.savefig('../figs/gauss_cdf.pdf')
plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
#plt.show() #opening the plot window

