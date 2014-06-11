import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools

inFile = open("/Users/Amanda/Documents/Research/mc_dy.txt", "r")
#inFile = open("/home/bellis/matts-work-environment/python/CMS_convert_csv_to_hep_tools_format/dimuons_hep_format.dat")

print "Reading in the data...."
collisions = hep_tools.get_collisions(inFile)


#if count % 1000 == 0:
    #print count
    
print len(collisions)


nmuons = []
massmuons = []
newmass = []
twopos = []
twoneg = []
opp = []

count = 0
for collision in collisions:
    
    if count%1000==0:
        print count

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
            
            
            energy = energy1 + energy2
            #print energy
            px = px1+ px2
            #print px
            py = py1 + py2
            pz = pz1 + pz2
            #p4 = energy + px + py + pz
            totmass = np.sqrt(energy**2 - (px**2 + py**2 + pz**2)) 
            if totmass == totmass:
                newmass.append(totmass)
                #print newmass
            #for i in range (0, len(newmass)):
                #newmass[i]
                
                
                
                
############ Three seperate plots ##########
    #print muons
            if firstmuon[4] == secondmuon[4] and firstmuon[4] == 1:
                if totmass == totmass:
                    #print firstmuon[4]
                    twopos.append(totmass)
                    #print twopos
            elif firstmuon[4] == secondmuon[4] and firstmuon[4] == -1:
                if totmass == totmass:
                    twoneg.append(totmass)
                #print twopos, twoneg
            elif firstmuon[4] + secondmuon[4] == 0:
                if totmass == totmass:
                    opp.append(totmass)




# Finding the parctile made of two muons            
#            masstot = mass1 + mass2
#            if masstot == masstot:
#                totalmass.append(masstot)
#                #for i in range (0,10):
#                #print masstot
#                for i in range (0,2):
#                   #print masstot[i]
   
      
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
plt.hist(massmuons,bins=200)

plt.xlabel('Mass')
plt.ylabel('Muons')
#plt.xlim(.07,.09)

#print massmuons[0:10]
#print np.mean(massmuons)

fig = plt.figure()
plt.hist(newmass,bins=200)

###############
fig = plt.figure()
plt.hist(twopos,bins=200)

fig = plt.figure()
plt.hist(twoneg,bins=200)

fig = plt.figure()
opp = np.array(opp)
plt.hist(opp,bins=200)

plt.show()


