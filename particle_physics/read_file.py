import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools 

f = open(sys.argv[1])

print "Reading in the data...."
collisions = hep_tools.get_collisions(f)

print len(collisions)

count = 0
for collision in collisions:

    jets = collision[0]
    muons = collision[1]
    electrons = collision[2]
    photons = collision[3]
    met = collision[4]

    print "# of jets: %d" % (len(jets))

    count += 1
