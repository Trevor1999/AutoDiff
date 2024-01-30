#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:47:48 2024

@author: trevorcrider
"""

import numpy as np
from DualNumbers import DualNumber

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

x0 = DualNumber.convertarr(x0)

F = np.zeros((6,6), dtype=np.double)

for i in range(6):
    x0[i].d = 1
    xdot = CalcXdot(0,x0)
    F[:,i] = DualNumber.deconvert(xdot, False)
    x0[i].d = 0

xdot_true = DualNumber.deconvert(xdot, True)

    
    
    