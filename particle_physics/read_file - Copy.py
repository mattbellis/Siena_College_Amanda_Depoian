import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools 

inFile = open("/Users/Amanda/Documents/Research/mc_ttbar.txt", "r")

print "Reading in the data...."
collisions = hep_tools.get_collisions(inFile)

print len(collisions)

numjets = []

count = 0
for collision in collisions:

    jets = collision[0]
    muons = collision[1]
    electrons = collision[2]
    photons = collision[3]
    met = collision[4]

    print "# of jets: %d" % (len(jets))

    count += 1
    
    number = len(jets)
    numjets.append(number)

fig = plt.figure()
plt.hist(numjets)

ply.show()