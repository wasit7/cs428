# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 10:49:13 2014

@author: Wasit
"""

#minhash
import cv2
import numpy as np
from scipy.ndimage import filters
from matplotlib import pyplot as plt
#histogram
img =cv2.imread('../img/scoliosis.jpg',0)
rmax,cmax=img.shape
n=2
dc, dr = cmax/n, rmax/n

# generate 2 2d grids for the x & y bounds
r, c = np.mgrid[slice(0, rmax, dr),
                slice(0, cmax, dc)]
#contruct integral image of HoG
imx = np.zeros(img.shape)
imy = np.zeros(img.shape)
#sigma for gausian window
sigma=2
filters.gaussian_filter(img, (sigma,sigma), (0,1), imx)
filters.gaussian_filter(img, (sigma,sigma), (1,0), imy)
#categorise directions of gradient into 4 groups (sw,se,nw and ne) 
I=np.zeros((rmax,cmax,2),dtype=np.uint16)
I[:,:,0] = (0<imx).astype(np.uint16).cumsum(0).cumsum(1)
I[:,:,1] = (0<imy).astype(np.uint16).cumsum(0).cumsum(1)
plt.imshow(I[:,:,0])
#rect is 4 coordinates of a rectangle
#rect=[r1c1 r2c2 r3c3 r4c4]
num_rect=(r.shape[0]-1)*(r.shape[1]-1)
rect=np.zeros((num_rect,8))
avg_rect=np.zeros((num_rect,1))
for i in range(0,r.shape[0]-1):
    for j in range(0,r.shape[1]-1):
        idx=j*(r.shape[0]-1)+i
        rect[idx,0]=r[i,j]
        rect[idx,1]=c[i,j]
        rect[idx,2]=r[i,j+1]
        rect[idx,3]=c[i,j+1]
        rect[idx,4]=r[i+1,j]
        rect[idx,5]=c[i+1,j]
        rect[idx,6]=r[i+1,j+1]
        rect[idx,7]=c[i+1,j+1]
        L1=I[rect[idx,0],rect[idx,1],0]
        L2=I[rect[idx,2],rect[idx,3],0]
        L3=I[rect[idx,4],rect[idx,5],0]
        L4=I[rect[idx,6],rect[idx,7],0]
        
        dr=r[i+1,j+1]-r[i,j]
        dc=c[i,j+1]-c[i,j]
        area=dr*dc
        
        avg_rect[idx]=float(L4-L2-L3+L1)/area