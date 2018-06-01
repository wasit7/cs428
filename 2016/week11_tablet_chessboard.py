# -*- coding: utf-8 -*-
"""
Created on Sat Nov 01 12:25:41 2014

@author: Wasit
"""


import numpy as np
from matplotlib import pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D

def showCemeraCoordinate(fig):
    fig.clear()
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
    plt.draw()     
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
nx=4#number of corner
ny=5
objp = np.zeros((nx*ny,3), np.float32)
objp[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1,2)



cap = cv2.VideoCapture(0)
fig = plt.figure()

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (nx,ny),1)

    # If found, add object points, image points (after refining them)
    if ret:
        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.
        objpoints.append(objp)

        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners)
        showCemeraCoordinate(fig)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (nx,ny), corners,ret)
    cv2.imshow('img',img)    
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()