import glob
import csv
import os
import math
import numpy as np
import ROOT
import ctypes
# The list rows1 is created to collect the rows of all the CVS files. It is a list of sublists where these sublists contain the rows of each file.
rows1 = []
for filename in glob.glob('emulsion-data-for-track-multiplicity/*_Vertex.csv'):
    file = open(filename)
    csvreader = csv.reader(file)
    # The list rows collects the rows of file 1 to be appended to the main list (rows1) and then file 2 and so on.  
    rows = []
    for row in csvreader:
        rows.append(row)
    rows1.append(rows)
vertex = []
for row in rows1:
    # # The data is given in the CSV files such that the multiplicity is given in the second row in the ninth entry. 	
    vertex.append(float(row[1][8]))  
h1 = ROOT.TH1F( 'h1', 'track multiplicity; multiplicity; Events', int(max(vertex)), 0., max(vertex) )
for xeach in vertex:
    h1.Fill(xeach)
c1 = ROOT.TCanvas()    
h1.Draw()
c1.Print("multiplicity.pdf")
