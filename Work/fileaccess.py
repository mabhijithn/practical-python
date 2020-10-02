# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
g = open('writefile.txt','wt')
g.write('some text')
g.close()
with open('foo.txt','rt') as f:
    data = f.read()
    
filename = 'foo.txt'
count = 0

with open(filename, 'rt') as f:
    for line in f:
        count = count+1        
        print('Line: ', count, line)
  
outfile = 'tmp.txt'        
with open(outfile, 'wt') as g:
    g.write('Hello World \n')

g = open(outfile, 'rt')
data = g.read()
print(data)
g.close()'''
import os.path as path

soccer538dir = '/home/abhijith/Documents/python/football-analyse/fivethirtyeight/data/soccer-spi'
filename = 'spi_matches_latest.csv'
f = open(path.join(soccer538dir, filename),'rt')

headers = next(f).strip()
headers = headers.split(',')

club = 'Liverpool'
count = 0
pts = 0
for line in f:
    if count>10:
        break
    row = line.split(',')
    year = int(row[0])
    if year==2020:
        if club in row:
            idx = row.index(club)
            if idx==4:
                probs = [float(row[8]),float(row[10]),float(row[9])]             
            else:
                probs = [float(row[9]),float(row[10]),float(row[8])]
            mx_prob = probs.index(max(probs))
            if mx_prob==0:
                pts = pts+3
            elif (mx_prob==1):
                pts = pts+1
print('Projected PL points for', club,'is', pts)            
f.close()
        