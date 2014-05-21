import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools

# On Amanda's machine
#inFile = open("/Users/Amanda/Documents/Research/mc_dy.txt", "r")
# On Matt's machine
inFile = open("/home/bellis/shdnbi2013_machinelearning/resources/mc_dy.txt", "r")

print "Reading in the data...."
collisions = hep_tools.get_collisions(inFile)

print len(collisions)

nmuons = []
massmuons = []
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


    # Finding the mass of a muon
    for muon in muons:
        energy = muon[0]
        px = muon[1]
        py = muon[2]
        pz = muon[3]
        mass = np.sqrt(energy**2 -(px**2 + py**2 + pz**2))
        if mass == mass:
            massmuons.append(mass)
        
    #print np.isnan(mass)
    
    
#    fig = plt.figure()
#    plt.hist(mass)
#    plt.xlabel('Mass')
#    plt.ylabel('Muons')
#    plt.xlim(0,1)
    
    
############# Histogram for the number of muons in each collision  ##########  

    
    data = (len(muons))
    nmuons.append(data)
    #print data
#print nmuons   
nmuons = np.array(nmuons)   
nmuons[nmuons==2]   
print (len(nmuons[nmuons==2]))
fig = plt.figure()    
plt.hist(nmuons)

plt.xlabel('Muons')
plt.ylabel('Collisions')
plt.xlim(-1,5)

############# end histogram of the number of muons in a collision ############

##################### Histogram for the mass of a muon ######################



fig = plt.figure()
plt.hist(massmuons,bins=100)

plt.xlabel('Mass')
plt.ylabel('Muons')
#plt.xlim(.07,.09)

print massmuons[0:10]
print np.mean(massmuons)



plt.show()



   
