
"""
Created on Mon May 19 14:03:26 2014

@author: Amanda
"""
import pylab
import numpy as np


# Bellis changes
fig = pylab.figure()

x1= np.array([0,1,2,3,4,5,6,7,8])
y1 = np.array([100,46,20,11,7,2,1,1,0])
y1err = np.sqrt(y1)
pylab.errorbar(x1,y1,yerr=y1err,fmt='o',color='r')

x2 = np.array([0,1,2,3,4,5,6,7,8])
y2 = np.array([100,48,25,13,7,2,1,1,0])
y2err = np.sqrt(y2)
pylab.errorbar(x2,y2,yerr=y2err,fmt='o',color='b')

x3 = np.array([0,1,2,3,4,5,6,7,8])
y3 = np.array([100,51,27,14,7,2,1,0,0])
y3err = np.sqrt(y3)
pylab.errorbar(x3,y3,yerr=y3err,fmt='o',color='c')

x4 = np.array([0,1,2,3,4,5,6,7,8])
y4 = np.array([100,52,30,10,5,2,1,1,0])
y4err = np.sqrt(y4)
pylab.errorbar(x4,y4,yerr=y4err,fmt='o',color='k')
pylab.plot(x4,y4,'go')

x5 = np.array([0,1,2,3,4,5,6,7,8])
y5 = np.array([100,59,28,12,4,1,1,1,0])
y5err = np.sqrt(y5)
pylab.errorbar(x5,y5,yerr=y5err,fmt='o',color='g')
pylab.plot(x5,y5,'co')

xtot = x1
ymean = (y1+y2+y3+y4+y5)/5.0
ystddev = 0.0
for y in [y1,y2,y3,y4,y5]:
    ystddev += (y-ymean)**2
ystddev = np.sqrt(ystddev)
ystddev[0] = 10 # The first number (100) is the same for all of them.

fig = pylab.figure()
pylab.errorbar(xtot,ymean,yerr=ystddev,fmt='o',color='r')
pylab.xlim(-1,9)

# Amanda's first attempt.
'''
lny = np.log(ymean)
fig = pylab.figure()
pylab.plot(lny,xtot,'bo')
pylab.ylim(-1,8)
pylab.xlim(-1,8)

slope = (ymean[-1]-ymean[0])/(xtot[-1]-xtot[0])
print "Slope = ", slope

intercept = ymean[2]-(xtot[2]*slope)
print "Intercept = ", intercept

print "y = ", np.exp(intercept), "*", "(e ** (",(slope), "* x))"
'''

N0 = 100
k = -0.5

xfit = np.linspace(0,8,1000)

# Your goal, is to pick the values of N0 and k so that 
# the chi2 is at a minimum.

yfit = N0*np.exp(k*xfit)
pylab.plot(xfit,yfit)

err = np.sqrt(ystddev)


for k in np.arange(-2,2,.001):
    for N0 in range (10,100,1):
        yA = N0*np.exp(k*xtot)
        if yA.any() == ystddev.any():
            chi2 = sum(((yA - ystddev)/err)**2)
            



pylab.show()
