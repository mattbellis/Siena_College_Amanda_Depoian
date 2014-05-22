
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
    print y
    ystddev += (y-ymean)**2
ystddev = np.sqrt(ystddev)
ystddev[ystddev==0] = np.sqrt(ymean[ystddev==0])
ystddev[ystddev==0] = 1.0
ystddev[0] = 10 # The first number (100) is the same for all of them.

print ymean
print ystddev
#exit()

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

N0 = 10
k = 0.5

xfit = np.linspace(0,8,1000)

# Your goal, is to pick the values of N0 and k so that 
# the chi2 is at a minimum.

err = ystddev

#print y1
#print y2
#print y3
#print y4
#print y5
#print ymean
#print err
err[err==0] = 1.0
#print err
#exit()



bestN0 = -999
bestk = -999

minchi2 = 10000000000000000

for k in np.arange(-2,2,.01):

    for N0 in np.arange (10,100,0.1):

        yA = N0*np.exp(k*xtot)
        chi2 = sum(((yA - ymean)/err)**2)

        if chi2<minchi2:
            print chi2
            minchi2 = chi2

            bestN0 = N0
            bestk = k
            


print "%f %f" % (bestN0,bestk)

yfit = bestN0*np.exp(bestk*xfit)
pylab.plot(xfit,yfit)

pylab.show()
