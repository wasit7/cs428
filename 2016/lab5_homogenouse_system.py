# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 12:03:55 2014

@author: Wasit
"""
from numpy import linalg as la
import numpy as np
# to solve for x from a homogeneous system Ax=0
A=np.array([[1,2,3],[3,6,11],[3,6,13],[3,6,14]])
U,s,V=la.svd(A)
#singular value is positive diagonal matrix
#if the last n elements on diagonal is near zero
#that means the last n columns of V are the null space
print("s: {}".format(s))
#compute the A*transpose(V)
A_times_V=np.dot(A,V.T)

print("\nA_times_V:\n {}".format(A_times_V))

x=np.reshape(V[-1,:],[-1,1])

print "\nAx:\n {}".format(np.dot(A,x))