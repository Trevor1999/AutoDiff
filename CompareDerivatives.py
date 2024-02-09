#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:11:12 2024

@author: trevorcrider
"""

import numpy as np
import matplotlib.pyplot as plt
from DualNumbers import DualNumber



def f(x):
    return x**3

def dfdx(x):
    return 3*x**2






x = np.linspace(-1,1,2500)

analytical = dfdx(x)

autodiff = f(DualNumber.convertarr(x, 1))
autodiff = DualNumber.deconvert(autodiff, False)

fig,ax = plt.subplots()

# ax.plot(x, analytical, label='Analytical', linestyle='--')
ax.plot(x, autodiff-analytical, label='Autodiff', linestyle='-.')

for i in range(7):
    h = 1*10**-i
    numerical = (f(x+h) - f(x-h) )/ (2*h)
    ax.plot(x, numerical-analytical, label=f'Central Diff h={h}', linestyle=':')
    
    


lgd = fig.legend()


