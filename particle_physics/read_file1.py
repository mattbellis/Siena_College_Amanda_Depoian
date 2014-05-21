import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools

inFile = open("/Users/Amanda/Documents/Research/mc_dy.txt", "r")

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


    if len(muons) >= 1:
        #print muons
        #print muons[0]
        firstmuon = muons[0]
        energy1 = firstmuon[0]
        #print "Energy1: ", energy1
        px1 = firstmuon[1]
        #print "Momentum in x direction (1): ", px1
        py1 = firstmuon[2]
        #print "Momentum in y direction (1): ", py1
        pz1 = firstmuon[3]
        #print "Momentum in z direction (1): ", pz1
        mass1 = np.sqrt(energy1**2 -(px1**2 + py1**2 + pz1**2))
        #print "Mass of a muon is (1)", mass1
        if mass1 == mass1:
            
            massmuons.append(mass1)
        
        if len(muons) == 2:
            #print muons
            #print muons[1]
            secondmuon = muons[1]
            energy2 = secondmuon[0]
            #print"Energy 2: ", energy2
            px2 = secondmuon[1]
            #print"Momentum in the x direction (2):", px2
            py2 = secondmuon[2]
            #print "Momentum in the y direction (2):", py2
            pz2 = secondmuon[3]
            #print "Momentum in the z direction (2):", pz2
            mass2 = np.sqrt(energy2**2 -(px2**2 + py2**2 + pz2**2))
            if mass2 == mass2:            
                massmuons.append(mass2)
            
            #print "Mass of a muon is (1)", mass1, "(2) ", mass2
            
        
   
      
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



   
