# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:03:27 2021

@author: kanch
"""


#A program that takes the number from the user 
#and tells wether the entered number is prime or not.

num=int(input("Enter number:"))   #input number

if num<=1:
    print('Prime numbers starts from 2')
    
elif num > 1:
    
   for i in range(2,num-1):
       
       if (num % i) == 0:       
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
           print(num,"is a prime number")
else:
   print(num,"is not a prime number")