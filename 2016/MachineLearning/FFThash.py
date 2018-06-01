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
from scipy import spatial

def G(x,mu,s):
    return 1.0/ np.sqrt(2.0*np.pi)*np.exp(((x-mu)**2)/(-2.0*s**2))
def getHash2(im_file):
    im = np.array(Image.open(im_file).convert('L'))
    f=np.fft.fft2(im)
    rmax,cmax=f.shape    
    sg=np.zeros((2*wd,wd))
    
    sg[0:wd,:]=np.abs(f[rmax-wd:rmax,0:wd])
    sg[wd:2*wd,:]=np.abs(f[0:wd,0:wd])
    
    fsg=np.zeros(wd)
    for b in xrange(wd):
        for r in xrange(wd):
            for c in xrange(wd):
                rad=np.sqrt(r**2+c**2)            
                fsg[b]=fsg[b]+sg[r,c]*G(rad,float(b),0.5)
        fsg[b]=fsg[b]/(np.pi*float(b+1))
    return fsg/np.linalg.norm(fsg)
def getHash(im_file):
    im = np.array(Image.open(im_file).convert('L'))
    f=np.fft.fft2(im)
    rmax,cmax=f.shape    
    sg_r=np.zeros((2*wd,wd))
    sg_r[0:wd,:]=np.abs(f.real[0:wd,0:wd])
    sg_r[wd:2*wd,:]=np.abs(f.real[rmax-wd:rmax,0:wd])
    sg_i=np.zeros((2*wd,wd))
    sg_i[0:wd,:]=np.abs(f.imag[0:wd,0:wd])
    sg_i[wd:2*wd,:]=np.abs(f.imag[rmax-wd:rmax,0:wd])
    
    bsg=np.zeros((2*wd,2*wd-2),dtype=bool)
    bsg[:,0:wd-1]=sg_r[:,0:wd-1]<sg_r[:,1:wd]
    bsg[:,wd-1:2*wd-2]=sg_i[:,0:wd-1]<sg_i[:,1:wd]
    
    return bsg
    
    f2=np.zeros((rmax,cmax))+1j*np.zeros((rmax,cmax))
    
    f2.real[0:wd,0:wd-1]=bsg[0:wd,0:wd-1]
    f2.imag[wd:2*wd,0:wd-1]=bsg[0:wd,wd-1:2*wd-2]
    f2.real[rmax-wd:rmax,0:wd-1]=bsg[wd:2*wd,0:wd-1]
    f2.imag[rmax-wd:rmax,0:wd-1]=bsg[wd:2*wd,wd-1:2*wd-2]
    #plt.close("all")
    plt.figure()
    plt.imshow(bsg,interpolation='none')
    plt.set_cmap("gray")
#    plt.figure()
#    im_b2=np.fft.ifft2(f2)
#    plt.imshow(im_b2.real,interpolation='none')
#    
#    plt.figure()
#    plt.imshow(im)
    
def js(b1,b2):
    #jaccard similarity
    return np.sum(np.bitwise_and(b1,b2))/float(np.sum(np.bitwise_or(b1,b2)))
def find(f,all_bsg,all_files):
    print "find: %s\n"%f
    bsg=getHash(f)
    for i,t in enumerate(all_bsg):
        print "sim: %.3f %s"%(js(bsg,t),all_files[i])
        
def find2(f,all_bsg,all_files):
    print "find: %s\n"%f
    fsg=getHash2(f)
    for i,t in enumerate(all_bsg):
        print "%03d sim: %.3f %s"%(i,np.dot(fsg,t),all_files[i])
def find3(tree,f,all_files):
    fsg=getHash2(f)
    d,ids=tree.query(fsg,k=10)
    for i,index in enumerate(ids):
        print "%03d dis: %.3f %s"%(index,d[i],all_files[index])
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
for f in all_files:
    print f
    bsg=getHash2(f)    
    all_bsg.append(bsg)
tree = spatial.KDTree(all_bsg)

import scipy.io as sio
sio.savemat('tree.mat',{'tree':tree})

