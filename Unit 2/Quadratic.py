# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:53:26 2021

@author: aditi
"""

'''
Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a*x^2 + b*x + c .

This function takes in four numbers and returns a single number.
'''
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a*(x**2) + b*x + c

evalQuadratic(3,3,2,9)