# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:02:35 2021

@author: aditi
"""
'''
EXERCISE 4

Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

This question is going to ask you what some simple loops print out. If you're asked what code like this prints:
'''
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

#5,4

'''
If a given loop will not terminate, write the phrase 'infinite loop' (no quotes) in the box. Recall that you can stop an infinite loop in your program by typing CTRL+c in the console.
'''
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

#0, 1, 2, 3, 4, 5, Outside of loop, 6

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

#infinite loop

num = 10
while num > 3:
    num -= 1
    print(num) 
    
#9, 8, 7, 6, 5, 4, 3

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')
#Note: If the command break is executed within a loop, 
#it halts evaluation of the loop at that point and passes control to the next expression. 
#Test some break statements inside different loops if you don't understand this concept!

#10, 9, 8, 7, Breaking out of loop, Outside of loop


num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

#infinite loop



'''
EXERCISE 5

Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

This question is going to ask you what some simple loops print out. If you're asked what code like this prints:
'''

num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

#5, 4

num = 10
for num in range(5):
    print(num)
print(num)

#0, 1, 2, 3, 4, 4

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 

#0.0, 1.0, 2.0, 3.0, 4.0

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
        
#0, Foo!, 4, 8, 12, 16, Foo!

for letter in 'hola':
    print(letter)  
    
#h, o, l, a

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

# Letter # 0 is S, 1


'''
EXERCISE 6

Try to answer the questions without running the code. 
Check your answers, then run the code for the ones you get wrong. 
You'll learn the most this way, by figuring things out, instead of just running the code and reading off the answers.
'''

myStr = '6.00x'

for char in myStr:
    print(char)

print('done')

'''
How many times does 6 print out?

1

How many times does . print out?

1
  
How many times does 0 print out?

2
  
How many times does x print out?

1
  
How many times does done print out?

1
'''

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

'''
How many times does H print out?

1
 
How many times does e print out? Disregard the letters in the word done.

2
   
How many times does l print out?

3
   
How many times does o print out? Disregard the letters in the word done.

1
   
How many times does ! print out?

2
   
How many times does done print out?

1
''' 

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 

'''
How many times does o print out? Disregard the o's in last two print statements.

0
   
How many times does M print out?

1
   
What will the value of the variable numVowels be?

11
   
What will the value of the variable numCons be?

-25
'''

'''
EXERCISE 7
'''

for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))



for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break


count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))



count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))



count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    