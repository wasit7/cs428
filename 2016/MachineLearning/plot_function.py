# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 13:56:29 2014

@author: Wasit
"""
#plot lagrange multiplier
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

# make these smaller to increase the resolution
dx, dy = 0.1, 0.1

# generate 2 2d grids for the x & y bounds
y, x = np.mgrid[slice(-3, 3 + dy, dy),
                slice(-3, 3 + dx, dx)]
f = x*y
plt.pcolor(x, y, f, cmap='RdBu')
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, f, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()