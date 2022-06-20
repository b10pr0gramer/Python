#!/usr/bin/env python
# coding: utf-8

# In[1]:


#JTMS-14
#a3_p1.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
int_nr = 428
print('the value over 8 places is {0:8d}'. format(int_nr))
 
float_nr1 = -98.6598894
print('the value over 10 places and floating precision of 4 is {0:10.4f}'. format(float_nr1))
 
character = '$'
print ('character is ', character)
 
float_nr2 = 56.486953
print('the value with a floating point precision of 2 is {:.2f}'. format(float_nr2))


# In[2]:


#JTMS-14
#a3_p1.py
#Balkrishna Baral
#b.baral@jacobs-university.de
first = input('Enter the number')
data = int(first)
if data%11 == 0:
    print('Divisible by 11')
else:
    print('not divisible by 11')


# In[3]:


#JTMS-14
#a3_p1.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
character = input('Enter the character')
asc = ord (character)
if 65 <= asc <= 90:
    print('uppercase')
else:
    print('lowercase')


# In[4]:


#JTMS-14
#a3_p1.py
#Balkrishna Baral
#b.baral@jacobs-university.de
n = 0
while n<11:
    print('n is', n)
    n += 1 # this part was outside the while loop due to indentation problem
print("that's it.")


# In[ ]:


#JTMS-14
#a4_p1.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
ch = input('Enter the character: ')
n = input('Enter the number: ')
num = int(n)
print(ch*num)


# In[ ]:


#JTMS-14
#a4_p2.py
#Balkrishna Baral
#b.baral@jacobs-university.de
asc =92
while asc>90:
    ch = input('Enter the upper case character: ')
    asc= ord(ch)
 
n = input('Enter the number: ')
 
num = int(n)
i=0
while i<=num:
    print(chr(asc+i))
    i=i+1


# In[ ]:


#JTMS-14
#a4_p3.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
asc = 1                                              # To start loop
while asc < 65 or asc > 90:                          # Condition to be uppercase
    ch = input('Enter the upper case character: ')   # Taking character input
    asc = ord(ch)
 
n = -1                                               # To start loop
while n < 0 or n > 32:                               # Range from question
    n = int(input('Enter the number: '))
 
i = asc
for i in range(asc, asc + n + 1):                    # Asc value of successive characters
    print(chr(i))


# In[ ]:


#JTMS-14
#a4_p4.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
i = 0
sum = 0
while i <= 10:
    n = int(input())          # Taking input
    if n == -9:               # Condition from question
        break
    i = i + 1                 # Counting the number of loop
    sum = sum + n             # Taking sum
 
 
print('the average is ', sum / i)


# In[ ]:


#JTMS-14
#a4_p5.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Taking input
n = int(input(''))
m = int(input(''))
c = input('')
 
# Defining a function
def print_rectange(n,m,c):
    i = 1
    for i in range(0,int(n)):          # n corresponds rows
        print(c*m)                     # m corresponds columns
 
# Calling the function
print_rectange(n,m,c)


# In[ ]:


#JTMS-14
#a4_p6.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Taking input
n = int(input(''))
m = int(input(''))
c = input('')
 
# Defining a function
def print_frame(n,m,c):
    i = 0
    k = m - 4                      # 4 corresponds to two character space
    print(c * m)                   # First line
    for i in range(n-2):           # Remaining lines = n-2
        print(c,' '*k,c)           # Number of spaces = k
    print(c * m)                   # Final line
 
# Calling a function
print_frame(n,m,c)


# In[ ]:


#JTMS-14
#a4_p7.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
n = input('Enter the string: ')       # Taking input
v = 0
for l in n:                           # Counting letters in string with for loop
      v = v+1
print("length of the string is:", v)


# In[ ]:


#JTMS-14
#a4_p8.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Taking the input
miles = float(input("Enter the miles: "))
 
# Defining a function
def convert(miles):
    factor = 1.609344
    value = miles * factor
    return value
 
# Printing outside the function
print('The km is : ', convert(miles))


# In[ ]:


#JTMS-14
#a5_p1.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
 
# Taking the input
cup = float(input("Enter the cups: "))
gallon = float(input("Enter the gallons: "))
 
# Defining a function
def to_litre(gallon,cup):
    factorg = 3.7854        # Given conversion factor
    factorc = 0.2366        # Given conversion factor
    gallon = gallon * factorg
    cup = cup * factorc
    return gallon, cup
 
 
# Printing outside the function
v = to_litre(gallon,cup)
print('The gallons and cups in litre are : ',v)


# In[ ]:


#JTMS-14
#a5_p2.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Taking input
s = input('Enter the string: ')
 
# Using len function
value = len(s)
 
# Printing the length
print('The length of the string is: ', value)


# In[ ]:


#JTMS-14
#a5_p3.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Taking Input
r = float(input("Enter the radius: "))
import math
 
# Defining a function
def volume_sphere(vol):
    vol = 4/3 * math.pi * (r*r*r)
    return vol
 
# Printing the volume
print('The volume is: ',volume_sphere(vol))


# In[ ]:


#JTMS-14
#a5_p4.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
import random
random . seed ()
minval = 1
maxval = 50
r = random . randint (minval , maxval )
found = False
count = 0
while not found :
    guess = int ( input (" Enter your guess : "))
    count = count + 1
    if r == guess :
        break
 
    elif guess < r:
        print (" Your guess is too small !", count)
    else :
        print (" Your guess is too high !", count)


# In[ ]:


#JTMS-14
#a5_p5.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Taking input
n = input('Enter the string:')
 
for i in range(0, len(n)):
    if i == 0:
        print(n[i])                 # First word
    else:
        print(' ' * (i - 1), n[i])


# In[ ]:


#JTMS-14
#a5_p6.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Defining a function
def count_vowels(s):
    count = 0
    for i in s:
        if i in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            count += 1
    return(count)
 
# Adding new line
str = input("Enter: " + '\n')
 
# Loop as long as there are vowel
while len(str) != 0:
    print("Vowel Counts: ", count_vowels(str))
    str = input("Enter: " + '\n')
    continue


# In[ ]:


#JTMS-14
#a5_p7.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Taking input
str = input("Enter string: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
 
# Number in the range of length of the string
while a and b not in list(range(len(str))) or a >= b:
    a = int(input("Enter valid a: "))
    b = int(input("Enter valid b: "))
print(str[a:b + 1])


# In[ ]:


#JTMS-14
#a5_p8.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
data = 'Python is a great programming language'
 
# Printing the list of words
print('the list is ', data.split())
# Printing to uppercase
print('To uppercase:', data.upper())
# Printing the position
print(data.find('programming'))
# Replacing g with G
print('Replacing g with G: ', data.replace('g', 'G'))


# In[ ]:


#JTMS-14
#a5_p9.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Taking input
text = input("Enter text: ")
s = input("To be replaced: ")
r = input("Replace with: ")
 
# printing the text
print(text)
 
# Using replace function
print(text.replace(s, r))


# In[ ]:


#JTMS-14
#a6_p1.py
#Balkrishna Baral
#b.baral@jacobs-university.de
 
# Reading input
f = open('B:\\input.txt', 'r')
 
# Defining output file
g = open('B:\\output.txt', 'w')
 
# Reading the characters
for line in f:
    a = ord(line[0])
    b = ord(line[1])
    product = a*b
    print(product, file=g)  # Writing result in file

