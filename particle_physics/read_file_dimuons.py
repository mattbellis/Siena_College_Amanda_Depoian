# -*- coding: utf-8 -*-
"""
Created on Mon Jun 02 12:49:05 2014

@author: Amanda
"""

import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools

inFile = open("/Users/Amanda/Documents/Research/dimuons_1000_collisions.txt", "r")
#inFile = open("/home/bellis/matts-work-environment/python/CMS_convert_csv_to_hep_tools_format/dimuons_hep_format.dat")

print "Reading in the data...."
collisions = hep_tools.get_collisions(inFile)

   
print len(collisions)



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


    count += 1


    if len(muons) >= 1:
        firstmuon = muons[0]
        energy1 = firstmuon[0]
        px1 = firstmuon[1]
        py1 = firstmuon[2]
        pz1 = firstmuon[3]
        
        if len(muons) == 2:
            secondmuon = muons[1]
            energy2 = secondmuon[0]
            px2 = secondmuon[1]
            py2 = secondmuon[2]
            pz2 = secondmuon[3]

            energy = energy1 + energy2
            px = px1+ px2
            py = py1 + py2
            pz = pz1 + pz2
            totmass = np.sqrt(energy**2 - (px**2 + py**2 + pz**2)) 
            if totmass == totmass:
                newmass.append(totmass)          
                

            if firstmuon[4] == secondmuon[4] and firstmuon[4] == 1:
                if totmass == totmass:
                    twopos.append(totmass)
            elif firstmuon[4] == secondmuon[4] and firstmuon[4] == -1:
                if totmass == totmass:
                    twoneg.append(totmass)
            elif firstmuon[4] + secondmuon[4] == 0:
                if totmass == totmass:
                    opp.append(totmass)



fig = plt.figure()
plt.hist(newmass,bins=1000)

fig = plt.figure()
plt.hist(twopos,bins=1000)

fig = plt.figure()
plt.hist(twoneg,bins=1000)

fig = plt.figure()
opp = np.array(opp)
plt.hist(opp,bins=1000)

plt.show()


