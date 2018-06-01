"""
===========================
The double pendulum problem
===========================

This animation illustrates the double pendulum problem.
"""

# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 300), ylim=(-2, 50))
ax.grid()

line, = ax.plot([], [], 'o', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

fps=25
dt=1.0/fps
#### begin simulation
sx=0
sy=0
ux=40
uy=30
t=0.0
#dt=0.1
g=-9.8
posx=[0]
posy=[0]
while sy>=0:
    t+=dt #t=t+dt
    ux=ux
    sx=sx+ux*dt
    uy=uy+g*dt
    sy=sy+uy*dt
    posx.append(sx)
    posy.append(sy)
print("ux:{} uy:{} sx:{} sy:{}".format(ux,uy,sx,sy))
#### end simulation
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, posx[i]]
    thisy = [0, posy[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(posx)),
                              interval=fps, blit=True, init_func=init)

# ani.save('double_pendulum.mp4', fps=15)
plt.show()