# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:46:03 2021

@author: aditi
"""
'''
Write a procedure called oddTuples, 
which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples 
on this input would return the tuple ('I', 'a', 'tuple').
'''

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    index = 0
    oddtup=()
    while index < len(aTup):
       oddtup = oddtup + (aTup[index],)
       index += 2
    return(oddtup)

#Alternative
def oddTuples2(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    # Here is another solution to the problem that uses tuple 
    #  slicing by 2 to achieve the same result
    return aTup[::2]


oddTuples((3, 19, 10, 12, 12, 9, 8, 9, 17, 0))