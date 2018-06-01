# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 14:14:45 2014

@author: Wasit
"""
from matplotlib import pyplot as plt 
import numpy as np
def g(x):
    #constraint function
    #0<x : g(x)=-log(x)
    #x<0 : g(x)=-log(-x)
    return -np.log(x)
def dg(x):
    return -1.0/x
def f(x):
    return 10-x*np.sin(x)
def df(x):
    return -x*np.cos(x)-np.sin(x)
x=np.arange(-50,50,0.1)
y=f(x)
plt.plot(x,y)
plt.hold(True)
xt=4.8
for i in xrange(10):  
    plt.plot(xt,f(xt),'xk')    
    #xt=xt-(f(xt)+g(xt))/(df(xt)+dg(xt))
    xt=xt-f(xt)/df(xt)
    