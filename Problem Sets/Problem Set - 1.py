# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 21:05:19 2021

@author: aditi
"""

'''
Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''

s = input("Enter your string")
count=0
for letter in s:
   if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    count += 1
print("Number of vowels: " + str(count))

'''
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

'''

s = input('Enter your string containing bob')
count = 0
for n in range(len(s)):
 if s[n:n+3] == 'bob':
  count+=1
print("Number of times bob occurs is: " + str(count))


'''
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
'''

s = 'abcbcd'
maxlength = 0
current = s[0]
longest = s[0]

for i in range(len(s) - 1):
      if s[i+1] >= s[i]:
         current += s[i+1]
         if len(current) > maxlength:
            maxlength = len(current)
            longest = current
      else:
         current = s[i+1]
      i += 1
print("The longest substring in alphabetical order is:" + longest)


