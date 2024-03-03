import glob
import csv
import os
import math
import numpy as np
import ROOT
import ctypes
# The list rows1 is created to collect the rows of all the CVS files. It is a list of sublists where these sublists contain the rows of each file.
rows1 = []
for filename in glob.glob('emulsion-data-for-charm-studies/*_Vertices.csv'):
    file = open(filename)
    csvreader = csv.reader(file)
    # The list rows collects the rows of file 1 to be appended to the main list (rows1) and then file 2 and so on.  
    rows = []
    for row in csvreader:
        rows.append(row)
    rows1.append(rows) 
# lenn list is created to calculate the length of decay from each file and collects all the entries in one list.   	
lenn = []
for row in rows1:
    length =  math.sqrt((float(row[1][1])-float(row[2][1]))**2 + (float(row[1][2])-float(row[2][2]))**2 + (float(row[1][3])-float(row[2][3]))**2) 	
    lenn.append(length)    
x = np.array(lenn)
h1 = ROOT.TH1F( 'h1', 'Length between vertices; length; Events', 10, 0., max(lenn) )
for xeach in x:
    h1.Fill(xeach)
c1 = ROOT.TCanvas()    
h1.Draw()
c1.Print("decay length.pdf")
