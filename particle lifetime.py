# -*- coding: utf-8 -*-
"""
Created on Wed May 28 11:58:12 2014

@author: Amanda
"""

import matplotlib.pylab as plt
import math
lifetime = [2.197*10**-6,2.906*10**-13,2.6*10**-8,8.4*10**-17,1.2380*10**-8,8.954*10**-11,5.116*10**-8,1.040*10**-12,1.638*10**-12,1.530*10**-12,7.2*10**-21,1.21*10**-20]
particles = ["$\mu^+$/$\mu^-$","$\ tau^+$/$\ tau^-$","$\pi^+$/$\pi^-$","$\pi^0$","K+/K-","K(short)","K(long)","D+/D-","B+/B-","B0","J/$\Psi$","Upsilon(1S)"]
p = [1,2,3,4,5,6,7,8,9,10,11,12]

lifetime = map(math.log10,lifetime)
print lifetime
fig = plt.figure()
plt.xticks(p,particles,fontsize = 8)
plt.scatter(p, lifetime, color="red", marker="o")

plt.title("The lifetime of particles")

plt.xlabel("Particle")
plt.ylabel("Lifetime")

plt.show()