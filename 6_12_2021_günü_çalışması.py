# -*- coding: utf-8 -*-
"""6.12.2021 günü çalışması

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VRZ4FuXxpm_CnXKb-wq9PofitZFmFUYC

Exercise -74
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:
Input: nums = [1,2,3,4]
Output: 2
Example 3:
Input: nums = [1,1,1,1]
Output: 0
"""

def harmonious(liste):
  new=[]
  x=sorted(set(liste))
  for i in range(1,len(x)):
    if abs(x[i]-x[i-1])==1:
      new.append(liste.count(x[i]) + liste.count(x[i-1]))
  if len(new)!=0:
     print(max(new))
  else:
     print(0)     

harmonious([1,3,2,2,5,2,3,7] )

[1,3,2,2,5,2,3,7]

There is an array with some numbers. All numbers are equal except for one. Try to find it!
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
This is the first kata in series:
Find the unique number (this kata)
Find the unique string
Find The Unique

def find_uniq(liste):
  for i in liste:
    if liste.count(i)==1:
      return i
find_uniq([ 1, 1, 1, 2, 1, 1 ])



"""Exercise-77
Enough is enough!
Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?
Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
Example
  delete_nth ([1,1,1,1],2) # return [1,1]
  
  delete_nth ([20,37,20,21],1) # return [20,37,21]
:c2df723deb5de5cf:
1


"""

def delete_nth(liste,n):
  x=set(liste)
  new=[]
  for i in x:
      if i not in new:
        new.append(i)
  while new.count(i)<n:
    new.append(i)      
  return new
delete_nth([1,1,1,1],3) 
delete_nth ([20,37,20,21],1)



"""xercise-78
Write a program, that takes in a positive parameter num and 
returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
Example 
39 --> returns 3, because 3*9 = 27 , 2*7 = 14 , 1*4 = 4 and 4 has only one digit

999 --> returns 4, because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12 and finally 1*2 = 2 

4 --> return 0 , because 4 is already one digit number
"""

def digit_(n):
 x=1
 count=0
 while len(str(n))>1:
   for i in str(n):
     x*=int(i)
     n=x
   x=1   
   count+=1
 return count


digit_(999)

Exercise-87
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

def pig_it(sentence):
  a=sentence.split()
  new=[]
  for i in a:
    if i.isalpha():
      i=i[1:]+i[:1]+"ay"
      new.append(i)
    else:
      new.append(i)
  return " " .join(new ) 
pig_it('Pig latin is cool') 
pig_it('Hello world !')

Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(n):
  x=n.lower()
  for i in x:
    if  x.count(i)==1:
      print(n[x.index(i)])
      break
    else:
      return "none"
first_non_repeating_letter("sTress")

[0, 0, 0, 0, 4, 0, 0, 0, 0] ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]

[0, 0, 0, 3, 0, 0, 0] ➞ [0, 1, 2, 3, 2, 1, 0]

[0, 0, 2, 0, 0] ➞ [0, 1, 2, 1, 0]

[0] ➞ [0]

balon=[0, 0, 0, 0, 4, 0, 0, 0, 0] 
print([i for i in range(max(balon))]+[i for i in range(max(balon),-1,-1)])

sample = [1, 0, 1, 2, 0, 1, 3]
output = [1, 1, 2, 1, 3, 0, 0]

sample=[1, 0, 1, 2, 0, 1, 3]
count=0
for i in sample:
  if i==0:
    sample.remove(i)
    count+=1
while sample.count(0)<count:    
   sample.append(0)    
sample

