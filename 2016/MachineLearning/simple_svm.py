# -*- coding: utf-8 -*-
"""
Created on Sat Dec 06 12:21:15 2014

@author: Wasit
"""
import numpy as np
from matplotlib import pyplot as plt
x=np.array([[1,1],[-1,-1]])
y=np.array([1,-1])

#unknown parameter
w=np.zeros(2)
b=np.zeros(2)
a=np.zeros(len(y))

plt.figure(1)
plt.axis([-5, 5, -5, 5])
plt.hold(True)
plt.grid(True)
for i,yi in enumerate(y):
    if yi<0:    
        plt.plot(x[i,0],x[i,1],'ob')
    else:
        plt.plot(x[i,0],x[i,1],'sr')
    