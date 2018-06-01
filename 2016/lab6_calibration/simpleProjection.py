# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 12:37:42 2014

@author: Wasit
"""
import numpy as np
from numpy import linalg as LA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#the script defined translation and rotation
#the camera projection is represented in camera coordinates
# as below extrinsic= [R|t]
# q_cameara = R*q_world + t
#However, it is easier to represent camera axes in world coordinate first
# q_world=R^T(q_camera - t)
# 
# U = R*[1 0 0]
# U = R1
Q=np.array([[0,0,0],[1,0,0],[0,1,0],[0,0,1]]).T
t=np.array([10,20,10])
R3=-t/LA.norm(t)
R2s=np.array([0,0,-1])
R2=R2s-np.dot(R3,R2s)*R3 #Gram–Schmidt process
R2=R2/LA.norm(R2)
R1=np.cross(R2,R3)

R=np.zeros((3,3))
R[0,:]=R1
R[1,:]=R2
R[2,:]=R3


plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

Qo=Q[:,0]
Qx=Q[:,1]
Qy=Q[:,2]
Qz=Q[:,3]

plt.hold(False)
ax.scatter(Qo[0],Qo[1],Qo[2],marker='o')
plt.hold(True)

ax.scatter(Qx[0],Qx[1],Qx[2],marker='x',color='r')
ax.scatter(Qy[0],Qy[1],Qy[2],marker='x',color='g')
ax.scatter(Qz[0],Qz[1],Qz[2],marker='x',color='b')


ax.scatter(t[0],t[1],t[2],marker='.')
U=t+R[0,:]
V=t+R[1,:]
W=t+R[2,:]
ax.scatter(U[0],U[1],U[2],marker='+',color='r')
ax.scatter(V[0],V[1],V[2],marker='+',color='g')
ax.scatter(W[0],W[1],W[2],marker='+',color='b')

plt.show()
ax.auto_scale_xyz([0, 10], [0, 10], [0, 10])



Rt=np.zeros((3,4))
Rt[:,0:3]=R.T
Rt[:,3]=-np.dot(R.T,t)
K=np.array([[10,0,0],
            [0,10,0],
            [0,0,10]])
P=np.dot(K,Rt)

qo=np.append(Qo,1)
qx=np.append(Qx,1)
qy=np.append(Qy,1)
qz=np.append(Qz,1)

po=np.dot(P,qo)
po=po/po[2]

px=np.dot(P,qx)
px=px/px[2]

py=np.dot(P,qy)
py=py/py[2]

pz=np.dot(P,qz)
pz=pz/pz[2]

plt.figure()
plt.hold(True)
plt.plot(po[0],po[1],marker='o',color='b')
plt.plot(px[0],px[1],marker='x',color='r')
plt.plot(py[0],py[1],marker='x',color='g')
plt.plot(pz[0],pz[1],marker='x',color='b')
#plt.axis([-2, 2, -2, 2])
plt.gca().invert_yaxis()