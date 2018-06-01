# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 15:36:09 2014

@author: Wasit
"""
#FFt
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os

# read image to array
rootdir="../img"
all_files=[]
for root, dirs, files in os.walk(rootdir):
    for f in files:
            if f.endswith('jpg'):
                all_files.append(os.path.join(root,f))
#    for subdir in dirs:
#        for iroot,idirs,ifiles in os.walk(os.path.join(root,subdir)):
#            for f in ifiles:
#                if f.endswith('jpg'):
#                    all_files.append(os.path.join(iroot,f))
wd=50
all_bsg=[]
plt.set_cmap("jet")
for im_file in all_files:
    print im_file
    im = np.array(Image.open(im_file).convert('L'))
    f=np.fft.fft2(im)
    rmax,cmax=f.shape    
    
    f2=np.zeros((rmax,cmax))+1j*np.zeros((rmax,cmax))
    
    f2[0:wd,0:wd-1]=f[0:wd,0:wd-1]
    f2[rmax-wd:rmax,0:wd-1]=f[rmax-wd:rmax,0:wd-1]
    sg=np.zeros((2*wd,wd))
    sg[wd:2*wd,:]=np.log(np.abs(f2[0:wd,0:wd])+1)
    sg[0:wd,:]=np.log(np.abs(f2[rmax-wd:rmax,0:wd])+1)
    #plt.close("all")
    plt.figure(1)
    plt.imshow(np.log(sg.real),interpolation='none')
    plt.figure(2)
    im_b2=np.fft.ifft2(f2)
    plt.imshow(im_b2.real,interpolation='none')
    plt.ginput(1)

