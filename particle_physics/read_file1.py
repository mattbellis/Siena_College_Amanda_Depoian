import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools1 

inFile = open("/Users/Amanda/Documents/Research/mc_dy.txt", "r")

print "Reading in the data...."
collisions = hep_tools1.get_collisions(inFile)

print len(collisions)

count = 0
for collision in collisions:

    jets = collision[0]
    muons = collision[1]
    electrons = collision[2]
    photons = collision[3]
    met = collision[4]

    #print "# of jets: %d" % (len(jets))

    count += 1
    #print "# of muons: %d" % (len(muons))
    
    
    
# Histogram for the number of muons in each collision    

    fig = plt.figure()
    data = (len(muons))
    
    
    #plt.hist(data)

    plt.xlabel('Muons')
    plt.ylabel('Collision')
    plt.xlim(-1,5)
    plt.ylim(0,100)

    plt.show()