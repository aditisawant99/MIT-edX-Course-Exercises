# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:31:50 2021

@author: aditi
"""

'''
Write a Python function, square, that takes in one number and returns the square of that number.

This function takes in one number and returns one number.

'''

def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    return x*x

square(9)


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


'''
Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

You should use the square procedure that you defined in an earlier exercise (you don't need to redefine square in this box; when you call square, the grader will use our definition).

This function takes in one number and returns one number.
'''

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(x*x)



'''
Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.
'''
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x%2 == 1


'''
Write an iterative function iterPower(base, exp) that calculates the exponential  by simply using successive multiplication. For example, iterPower(base, exp) should compute  by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer  0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.
'''
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while exp>0:
       result *= base
       exp -= 1
    return result

'''
In Problem 1, we computed an exponential by iteratively executing successive multiplications. We can use the same idea, but in a recursive function.

Write a function recurPower(base, exp) which computes base^exp by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; exp will be an integer >= 0. It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed.
'''

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp ==0 :
      return 1
    else:
      return base * recurPower(base,exp-1)


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
       
  

'''
The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.
'''

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b==0:
      return a
    else:
      return gcdRecur(b,a%b)


'''
We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.
'''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    val1 = len(aStr)//2
    if aStr == "":
        return False
    elif len(aStr) <=1 and char != aStr[0]:
        return False
    elif char == aStr[val1]:
        return True
    elif char < aStr[val1]:
        val2 = aStr[:val1]
        return isIn(char,val2)
    elif char > aStr[val1]:
        val3 = aStr[val1:]
        return isIn(char, val3)
    elif char != val2 and char != val3:
        return False