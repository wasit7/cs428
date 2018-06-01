# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 17:13:06 2014

@author: Wasit
"""
#computer vision
#newton method
import numpy as np
from matplotlib import pyplot as plt

x=1.0

for i in xrange(50):
    f= 1.0 + 3.0*x**2.0 + 5.0*x**3.0
    print "x: %.3f, f:%.3f"%(x,f)
    fx=4.0*x + 9.0*x**2.0
    x=x-f/fx

