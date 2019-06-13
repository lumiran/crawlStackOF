# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:01:43 2019

@author: lumir
"""
import csv
import pandas as pd
import numpy as np
filename = ['1.csv','2.csv','3.csv','4.csv']


all_url = []
count30 = 0
count0 = 0
for j in range(4):
    file = filename[j]
    csvfile = csv.reader(open(file,encoding = 'utf-8'))
    for i,stu in enumerate(csvfile):
        if i == 0:
            continue
        if int(stu[1])>=30:
            count30+=1
        if int(stu[1])==0:
            count0+=1
        else:    
            all_url.append(stu[2])
    
print('Sparsity:',count0/)

    
        
#    1012620
