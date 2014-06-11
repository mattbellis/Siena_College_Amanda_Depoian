import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools 

inFile = open("/Users/Amanda/Documents/Research/mc_ttbar.txt", "r")
#inFile = open("/home/bellis/shdnbi2013_machinelearning.BAK2/resources/particle_physics/data/mc_ttbar.txt", "r")
#inFile = open("/home/bellis/shdnbi2013_machinelearning.BAK2/resources/particle_physics/data/data.txt", "r")

print "Reading in the data...."
collisions = hep_tools.get_collisions(inFile)

print len(collisions)

numjets = []
massjets = []
#massjets1 = []
#massjets2 = []
#massjets3 = []
#jets1 = []
#jets2 = []
#jets3 = []
massW = []

count = 0
for collision in collisions:

    jets = collision[0]
    muons = collision[1]
    electrons = collision[2]
    photons = collision[3]
    met = collision[4]

    #print "# of jets: %d" % (len(jets))



    
        
        
    count += 1
    
    number = len(jets)
    numjets.append(number)
    
    for i in range (0,number):
        for j in range (i+1,number):
            for k in range (j+1, number):
                #jets1.append(jets[i])
                #jets2.append(jets[j])
                #jets3.append(jets[k])
                
                #print jets[i][0]
                
                energy1 = jets[i][0]
                px1 = jets[i][1]
                py1 = jets[i][2]
                pz1 = jets[i][3]
                #mass1 = np.sqrt(energy1**2 -(px1**2 + py1**2 + pz1**2))
                #print mass1
                
                #if mass1 == mass1:
                 #   massjets1.append(mass1)
            
                energy2 = jets[j][0]
                px2 = jets[j][1]
                py2 = jets[j][2]
                pz2 = jets[j][3]
                #mass2 = np.sqrt(energy2**2 -(px2**2 + py2**2 + pz2**2))
                #print mass2
                
                #if mass2 == mass2:
                  #  massjets2.append(mass2)
                        
                
                energy3 = jets[k][0]
                px3 = jets[k][1]
                py3 = jets[k][2]
                pz3 = jets[k][3]
                #mass3 = np.sqrt(energy3**2 -(px3**2 + py3**2 + pz3**2))
                #print mass3                
                
                #if mass3 == mass3:
                 #   massjets3.append(mass3)
                mass = np.sqrt((energy1+energy2+energy3)**2 -((px1+px2+px3)**2 + (py1+py2+py3)**2 + (pz1+pz2+pz3)**2))
                #print mass   
                
                #if mass == mass:
                massjets.append(mass)
                #print massjets   
                
                
######## finding the W boson #########

    for L in range (0,number):
        for M in range (L+1, number):
            
            energyL = jets[L][0]
            pxL = jets[L][1]
            pyL = jets[L][2]
            pzL = jets[L][3]
            
            energyM = jets[M][0]
            pxM = jets[M][1]
            pyM = jets[M][2]
            pzM = jets[M][3]
            
            massLM = np.sqrt((energyL+energyM)**2 -((pxL+pxM)**2 + (pyL+pyM)**2 + (pzL+pzM)**2))
            massW.append(massLM)
               
               
fig = plt.figure()
plt.hist(numjets)

#print len(massjets)
#print massjets
fig = plt.figure()
plt.hist(massjets, bins = 100)



fig = plt.figure()
plt.hist(massW, bins = 500, range = (0,500))

plt.show()




# The mass of the Top Quark = 173.34 +- 0.27 (stat) +- 0.71 
