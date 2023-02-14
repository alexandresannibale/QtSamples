# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:54:13 2023

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

dt = 1e-5
f= 1000
time = 2/1000
points = time/dt

t = np.arange(0, points ) * dt

y = np.sin(2*np.pi *f* t)

X = np.array([t,y])
X = X.T
plt.close()
plt.plot(t,y)

np.savetxt("qtNumpySinusiodData.txt", X)