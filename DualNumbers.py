# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:03:43 2024

@author: trevor
"""


import numpy as np

class DualNumber:

    def __init__(self, Primal, Dual):
        """

        Parameters
        ----------
        Primal : TYPE
            DESCRIPTION.
        Dual : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.p = Primal
        self.d = Dual
    
    def convertarr(arr):
        """
        

        Parameters
        ----------
        arr : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        outarr = np.zeros((np.size(arr)), dtype=object)
        for i,x in enumerate(np.nditer(arr)):
            outarr[i] = DualNumber(x, 0)
        return outarr.reshape(np.shape(arr))
    
    def deconvert(arr, primal=True):
        """
        Description
        -----------
        Takes a numpy array of DualNumbers and returns a numpy array with dtype of float64.
        The array will be constructed from either the dual or primal part of the dual numbers,
        depending on the input Primal.
        If Primal is True then the array will be made up of the primal part of the dual numbers
        If Primal is False then the array will be made up of the dual part of the dual numbers

        
        Parameters
        ----------
        arr : numpy.ndarray
        primal : boolean, default is True


        Returns
        -------
        numpy.ndarray

        """
        outarr = np.zeros((arr.size), dtype=np.double)
        for i,x in enumerate(np.nditer(arr, flags=['refs_ok'], op_dtypes=object)):
            outarr[i] = x.take(0).p if primal else x.take(0).d
        return outarr.reshape(arr.shape)
    
    def __add__(self, other):# DualNumber + other
        """
        
        
        """
        if isinstance(other, DualNumber):
            return DualNumber(self.p+other.p, self.d+other.d)
        elif isinstance(other, float) or isinstance(other, int):
            return DualNumber(self.p + other, self.d)
        
    def __radd__(self,other):# other + DualNumber
        if isinstance(other, DualNumber):
            return DualNumber(self.p+other.p, self.d+other.d)
        elif isinstance(other, float) or isinstance(other, int):
            return DualNumber(self.p + other, self.d)
    
    
    def __sub__(self,other):
        if isinstance(other, DualNumber):
            return DualNumber(self.p-other.p, self.d-other.d)
        elif isinstance(other, float) or isinstance(other, int):
            return DualNumber(self.p - other, self.d)


    def __rsub__(self,other): # float/int/DN - DualNumber
        if isinstance(other, int) or isinstance(other ,float):
            return DualNumber(other - self.p, -self.d)
        elif isinstance(other, DualNumber):
            return DualNumber(other.p - self.p, other.d - self.d)
    
    def __str__(self):
        return f'Primal: {self.p}, Dual: {self.d}'

    def __repr__(self):
        return f'({self.p},{self.d})'

    def __mul__(self, other): # DualNumber * other
        if isinstance(other, DualNumber):
            p = self.p*other.p
            d = self.d*other.p + self.p*other.d
            return DualNumber(p,d)
        elif isinstance(other, float) or isinstance(other, int):
            p = self.p*other
            d = self.d*other
            return DualNumber(p,d)
        elif isinstance(other, np.ndarray):
            outarr = np.zeros((other.size,), dtype=other.dtype)
            for i,x in enumerate(other):
                outarr[i] = self * x
            return outarr.reshape(other.shape)


    def __rmul__(self,other):
        if isinstance(other, DualNumber):
            p = self.p*other.p
            d = self.d*other.p + self.p*other.d
            return DualNumber(p,d)
        elif isinstance(other, float) or isinstance(other, int):
            p = self.p*other
            d = self.d*other
            return DualNumber(p,d)
        elif isinstance(other, np.ndarray):
            pass  #need to implement rmul
            
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
        elif isinstance(other, DualNumber):
            p = self.p ** other.p
            d = other.p * self.p**(other.p-1)*self.d + np.log(self.p)*self.p**other.p * other.d
        return DualNumber(p,d)

    def __rpow__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            p = other**self.p
            d = other**self.p * np.log(other) * self.d
        return DualNumber(p, d)
    
    
    def copy(self):
        return DualNumber(self.p, self.d)

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
    
    def log(self):
        p = np.log(self.p)
        d = self.d / p
        return DualNumber(p,d)
    
    def exp(self):
        p = np.exp(self.p)
        d = p*self.d
        return DualNumber(p,d)
    
    
