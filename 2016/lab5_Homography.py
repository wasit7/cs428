from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# read image to array
im = np.array(Image.open('img/square0.jpg'))
# plot the image
plt.imshow(im)
plt.show()
plt.hold(True)
n=5
#q=[[qx,qy]]
q=np.array([ [0.0, 0.0, 1.0],[10.0, 0.0, 1.0], [10.0,10.0,1.0], [0.0, 10.0,1.0], [5.0,5.0,1.0]])
#u to the right, v downward
gin_uv=plt.ginput(n)

print gin_uv

#M = 0 0 0 pwqx pwqy pw pvqx pvqy pv
#    pwqx pwqy pw 0 0 0 puqx puqy pu
M=[]
          
for i in range(4):
    qx=q[i,0]
    qy=q[i,1]
    pu=gin_uv[i][0]
    pv=gin_uv[i][1]
    
    M.append([qx, qy, 1, 0, 0, 0, -pu*qx, -pu*qy, -pu])
    M.append([0, 0, 0, -qx, -qy, -1, pv*qx, pv*qy, pv])
    
    print(0, 0, 0, qx, qy, 1, pv*qx, pv*qy, pv)
    print(qx, qy, 1, 0, 0, 0, pu*qx, pu*qy, pu)

A=np.array(M).reshape(-1,9)
U,s,V=np.linalg.svd(A)

#H=H11 H12 H13 H21 H22 H23 H31 H32 H33
H=np.reshape(V[-1,:],(3,3))
p_new=np.dot(H,q.T)
plt.plot(p_new[0,:]/p_new[2,:],p_new[1,:]/p_new[2,:],'xb')
