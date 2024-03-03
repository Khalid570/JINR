import glob
import csv
import os
import math
import numpy as np
#import ROOT
import ctypes
import matplotlib.pyplot as plt
from numpy.linalg import norm
z = glob.glob('emulsion-data-for-track-multiplicity/*Tracks.csv')
#The list "lenn" is a collection of sublists and each sublist has 2 numbers: The first one is the angle made by the trackline with the x-axis and the second one is the angle made by the trackline with the Y-axis. 
lenn = []
for filename in z: 	
    file = open(filename)
    csvreader = csv.reader(file)
    for row in csvreader:
    	# Only the tracklines that have trType = 1 are of our interest. These are the tracklines of muons as described on CERN Open Data portal in this URL: https://opendata.cern.ch/record/3901 
        if row[0] == '1':
           # The data is given in the CSV files such that the fifth and the sixth elements of the row are the slopes of the trackline in the XZ and YZ planes, respectively. Thus, tan inverse is applied to get the angle made with the X-axis and the Y-axis. 
           lenn.append([math.degrees(math.atan(float(row[4]))),math.degrees(math.atan(float(row[5])))])
# The lists "x" and "y" are created to extract and separate the angles made with the X-axis and the Y-axis from the list "lenn".            
x = []
y = []
for i in range(len(lenn)):
    x.append(lenn[i][0])
for i in range(len(lenn)):
    y.append(lenn[i][1])

#The 3-D plot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(x, y, bins=10, range=[[min(x), max(x)], [min(y),max(y)]])

xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

dx = 2 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

plt.title("angles distribution")
plt.xlabel("angle with the X-axis")
plt.ylabel("angle with the Y-axis")

plt.savefig("3-dimensional angle distribution.pdf")
plt.show()

# The 2-D plot
plt.hist2d(x, y)
plt.title("angles distribution")
plt.xlabel("angle with the X-axis")
plt.ylabel("angle with the Y-axis")
plt.colorbar()

plt.savefig("2-dimensional angle distribution.pdf")
plt.show()

plt.close()
