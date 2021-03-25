# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:19:06 2021

@author: kanch
"""

#A Program that asks the user for a number.
#Depending on whether the number is even or odd, print out an appropriate message to the user.

num=int(input("Enter any number:"))

if num%2==0:
    print(num, " is even")
    print("Because",num, "will give yield 0 when",num,end="" "%2 is performed")

else:
    print(num, "is odd")   
    print("Because",num," will yields 1 when",num,end= "" "%2 is operated")