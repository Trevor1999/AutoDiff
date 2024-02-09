#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:47:48 2024

@author: trevorcrider
"""

import numpy as np
from DualNumbers import DualNumber
from scipy.integrate import solve_ivp
import time

def CalcXdot(t,X):
    ## Example: simple gravity model w/ drag on exponential atmosphere
    r = X[0:3]
    v = X[3:]
    
    mu = 398600.4418
    rmag = np.linalg.norm(r)
    alt = rmag - 6378
    rho = 1.225*np.exp(- alt / 65)
    
    
    drag_acc = -.5*rho*np.linalg.norm(v)*v*1000
    grav_acc = -mu*r / rmag**3
    

    vdot = drag_acc + grav_acc
    return np.concatenate((v, vdot))


x0 = np.array([6534, 556, -6845.353, 0, 0, 0] ,dtype=np.double)
# v = sqrt(r/mu) or? sqrt(mu/r)
x0[3:] = np.sqrt(398600.4418 / np.linalg.norm(x0)) * np.cross(x0[0:3], [0,0,1]) / np.linalg.norm(x0)

# x0 = DualNumber.convertarr(x0)

# F = np.zeros((6,6), dtype=np.double)

# for i in range(6):
#     x0[i].d = 1
#     xdot = CalcXdot(0,x0)
#     F[:,i] = DualNumber.deconvert(xdot, False)
#     x0[i].d = 0

# xdot_true = DualNumber.deconvert(xdot, True)

def dfdt_stm(t,X):
    State = X[0:6]
    Phi = X[6:].reshape((6,6))
    State = DualNumber.convertarr(State)
    F = np.zeros((6,6), dtype=np.double)
    
    for i in range(6):
        State[i].d = 1
        xdot = CalcXdot(t,State)
        F[:,i] = DualNumber.deconvert(xdot, False) # get dual part (partial derivative of xdot)
        State[i].d = 0
    xdot = DualNumber.deconvert(xdot, True) # get the real part (xdot)
    phidot = F @ Phi
    return np.concatenate((xdot, phidot.reshape(36,)))



x0_stm = np.concatenate((x0, np.eye(6).reshape((36,))))


t0 = time.perf_counter()
sol = solve_ivp(dfdt_stm,(0,3600), x0_stm)
print(f"time elapsed: {time.perf_counter() - t0}")




    