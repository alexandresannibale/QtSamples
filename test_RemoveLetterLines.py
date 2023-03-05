# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 22:55:38 2023

@author: Alexandre
"""

import numpy as np
#%%

def removeLetterLines(filename):
    with open(filename, "r") as fi:   
        n = 1
        S = []
        while n >0:
            s = fi.readline()
            n =  len(s)
            s = s.split()
            
            if arenumbers(s) == True:
                S.append(s)
                print(s)
    return S
    
#%%
def arenumbers(s):
    if s == []:
        return False
    else:
        for b in s:
          try:
              float(b)
          except:
              return False
      
        return True
#%%
M = np.array(removeLetterLines("data_test.txt"), dtype = float)   
print(M)



