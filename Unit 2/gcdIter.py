# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:56:00 2021

@author: aditi
"""

'''
The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
'''

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b%a==0:
      return a
    if a%b==0:
      return b
      
    if a<b:
     for i in range(a,1,-1):
         if a%i==0 and b%i==0:
            return i
    if b<a:
     for j in range(b,1,-1):
         if a%j==0 and b%j==0:
            return j
    else:
      return 1