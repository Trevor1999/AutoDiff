# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 09:14:33 2024

@author: TrevorAE
"""

## Test to calculate the state transition matrix

import numpy as np
from DualNumbers import DualNumber

A = np.array([[0,1],[-4,0]])
def calcxdot(t,state):
    return np.reshape(A @ state, (2,))


def RK45_step(t,state,dt):
    k1 = calcxdot(t,state)
    k2 = calcxdot(t + dt/2, state + k1*dt/2)
    k3 = calcxdot(t + dt/2, state + k2*dt/2)
    k4 = calcxdot(t + dt, state + dt*k3)
    return state + (k1+2*k2+2*k3+k4)*dt/6





x0 = DualNumber(3,1)
v0 = DualNumber(0,0)

s = np.array([x0,v0], dtype=object)

t = 0
dt = 1e-5

output = np.zeros((2,1000), dtype=object)
output[:,0] = s.copy()

for i in range(1,1000):
    output[:,i] = RK45_step(i, output[:,i-1], dt)
    t+=dt

print(f'numerical: {output[0,-1].d}, analytical: {np.cos(2*t)}')
print(f'numerical: {output[1,-1].d}, analytical: {-2*np.sin(2*t)}')



# exact solution

# x(t) = c1 * cos(2*t) + c2 * sin(2*t)
# c1 = 3
# c2 = 0



