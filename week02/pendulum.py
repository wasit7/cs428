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
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o', lw=2)
time_template = 'time:%.1fs, theta: %.1f'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

fps=25
dt=1.0/fps
def d2r(x):
  return x/180.0*np.pi
def r2d(x):
  return x/np.pi*180.0

#### begin simulation
theta= d2r(45) #angular displacement
omega= d2r(0)  #angular velocity
alpha= d2r(0)  #angular acceleration
m= 2.0 #kg
L= 1.0 #m
I= 4.0 #kg.m^2
g=9.8
t=0
posx=[0]
posy=[0]
list_theta=[theta]
for i in range(200):
    t+=dt #t=t+dt
    alpha=m*g*np.sin(theta)*L
    omega=omega+alpha*dt
    theta=theta+omega*dt
    sx=-L*np.sin(theta)
    sy=L*np.cos(theta)
    posx.append(sx)
    posy.append(sy)
    list_theta.append(r2d(theta))

#### end simulation
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, posx[i]]
    thisy = [0, posy[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt,list_theta[i]))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(posx)),
                              interval=fps, blit=True, init_func=init)

# ani.save('double_pendulum.mp4', fps=15)
plt.show()