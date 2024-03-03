import glob
import csv
import os
import math
import numpy as np
import ROOT
import ctypes
from numpy.linalg import norm
z = glob.glob('emulsion-data-for-charm-studies/*_TrackLines.csv')
z.sort()
lenn = []
for filename in z: 	
    file = open(filename)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        if row[0] == '10':
           rows.append(row)
    lenn.append(rows)

z1 = glob.glob('emulsion-data-for-charm-studies/*_Vertices.csv')
z1.sort()
rows1 = []   
  
for filename1 in z1:
    #print(filename1)
    file1 = open(filename1)
    csvreader = csv.reader(file1)
    for row1 in csvreader:
        if row1[0] == '1':
            rows1.append(row1)
#vertex_A
vertices = [] 
for vertex in rows1:
    vertex_vector = (float(vertex[1]), float(vertex[2]), float(vertex[3]))
    vertices.append(vertex_vector)  
 
#vertex_B
daughter_vector_B = []
for file1 in lenn:
    file_daughter_vector_B = []
    for row in file1: 
        daughter_vector_1 = (float(row[1]),float(row[2]),float(row[3]))
        file_daughter_vector_B.append(daughter_vector_1) 
    daughter_vector_B.append(file_daughter_vector_B)
            
#vertex_C 
daughter_vector_C = []
for file1 in lenn:
    file_daughter_vector_C = []
    for row in file1: 
        daughter_vector_1 = (float(row[4]),float(row[5]),float(row[6]))
        file_daughter_vector_C.append(daughter_vector_1) 
    daughter_vector_C.append(file_daughter_vector_C)  

#Vector_BC       
daughter_vector = []
for file1 in lenn:
    file_daughter_vector = []
    for row in file1: 
        daughter_vector1 = (float(row[4])-float(row[1]),float(row[5])-float(row[2]),float(row[6])-float(row[3]))
        file_daughter_vector.append(daughter_vector1) 
    daughter_vector.append(file_daughter_vector)
             
#Vector_AB
vector_A_B = []
for i in range(len(vertices)):
    vector_d = []
    for vectorB in daughter_vector_B[i]:
        vector_AB = np.subtract(vertices[i],vectorB)
        vector_d.append(vector_AB)
    vector_A_B.append(vector_d)

cp = []    
for i in range(len(daughter_vector)):
    for j in range(len(daughter_vector[i])):    
        x = np.cross(vector_A_B[i][j], daughter_vector[i][j])
        cp.append(x)
    
cr = []
for ls in cp:
    z = norm(ls,2)
    cr.append(z) 
    
cr1 = []    
       
for ls in daughter_vector:
    for vector in ls:
        z = norm(vector,2)
        cr1.append(z)
        
impact_parameter = []  
               
for i in range(len(cr)):
    z = cr[i]/cr1[i]
    impact_parameter.append(z)
        
h1 = ROOT.TH1F( 'h1', 'impact parameter; impact parameter; Tracks', 10, 0., max(impact_parameter) )

for xeach in impact_parameter:
    h1.Fill(xeach)
c1 = ROOT.TCanvas()    
h1.Draw()
c1.Print("impact parameter.pdf")
             
