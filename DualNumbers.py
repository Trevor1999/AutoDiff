# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:03:43 2024

@author: trevo
"""


import numpy as np

class DualNumber:

    def __init__(self, Primal, Dual):
        self.p = Primal
        self.d = Dual

    def __add__(self, other):

        return DualNumber(self.p+other.p, self.d+other.d)

    def __sub__(self,other):
        return DualNumber(self.p-other.p, self.d-other.d)

    def __str__(self):
        return f'Primal: {self.p}, Dual: {self.d}'

    def __repr__(self):
        return f'({self.p},{self.d})'

    def __mul__(self, other):
        if isinstance(other, DualNumber):
            p = self.p*other.p
            d = self.d*other.p + self.p*other.d
        elif isinstance(other, float) or isinstance(other, int):
            p = self.p*other
            d = self.d*other
        return DualNumber(p, d)

    def __rmul__(self,other):
        if isinstance(other, DualNumber):
            p = self.p*other.p
            d = self.d*other.p + self.p*other.d
        elif isinstance(other, float) or isinstance(other, int):
            p = self.p*other
            d = self.d*other
        return DualNumber(p, d)


    def __truediv__(self,other):
        if isinstance(other, DualNumber):
            p = self.p / other.p
            d = (self.d*other.p - self.p*other.d ) / other.p**2
        elif isinstance(other,float) or isinstance(other, int):
            p = self.p / other
            d = self.d / other
        return DualNumber(p,d)

    def __rtruediv__(self,other):
        if isinstance(other, DualNumber):
            p = other.p / self.p
            d = (self.p*other.d - self.d*other.p ) / self.p**2
        elif isinstance(other,float) or isinstance(other, int):
            p = other / self.p
            d = - self.d*other / self.p**2
        return DualNumber(p,d)

    def __pow__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            p = self.p**other
            d = self.d*(other)*(self.p**(other-1))
            return DualNumber(p,d)

    def __rpow__(self,other):
        pass

    def __neg__(self):
        p = -self.p
        d = -self.d
        return DualNumber(p,d)

    def cos(self):
        p = np.cos(self.p)
        d = -np.sin(self.p)*self.d
        return DualNumber(p,d)

    def sin(self):
        p = np.sin(self.p)
        d = np.cos(self.p)*self.d
        return DualNumber(p,d)
    def sqrt(self):
        p = np.sqrt(self.p)
        d = self.d/(2*p)
        return DualNumber(p,d)
