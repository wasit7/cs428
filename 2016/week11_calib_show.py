# -*- coding: utf-8 -*-
"""
Created on Sat Nov 01 14:31:46 2014

@author: Wasit
"""
import numpy as np
from matplotlib import pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)
ax.set_zlim(0,50)
ax.plot([0],[0],[0],'ok')
ax.plot([1],[0],[0],'sr')
ax.plot([0],[1],[0],'sg')
ax.plot([0],[0],[1],'sb')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
c=['r', 'g', 'b', 'c', 'm', 'y', 'k']
for i in xrange(len(objpoints)):
    R=np.zeros((3,3))
    t=tvecs[i]
    cv2.Rodrigues(rvecs[i],R)
    qw=objpoints[i].T
    qc=np.dot(R,qw)+t
    ax.scatter(qc[0,:],qc[1,:],qc[2,:],color=c[i%7])
