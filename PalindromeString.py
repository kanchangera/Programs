# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:10:14 2021

@author: kanch
"""

#Ask the user for a string and print out whether this string is a palindrome or not.
#A palindrome is a string that reads the same forwards and backwards.

string=input(("Enter a string:"))

if(string==string[::-1]):
    
      print("The string is a palindrome")
else:
    
      print("Not a palindrome!")