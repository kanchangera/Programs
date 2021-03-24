# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:03:27 2021

@author: kanch
"""

num=int(input("Enter number:")) 
if num > 1:
   for i in range(2,num-1):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
           print(num,"is a prime number")
else:
   print(num,"is not a prime number")