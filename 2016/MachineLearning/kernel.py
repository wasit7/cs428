# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 22:38:23 2014

@author: Wasit
"""
    
import numpy as np

def G(x,mu,s):
    return 1.0/ np.sqrt(2.0*np.pi)*np.exp(((x-mu)**2)/(-2.0*s**2))

from matplotlib import pyplot as plt
x=np.arange(0,10,0.1)
y=G(x,3,1)
plt.plot(x,y)