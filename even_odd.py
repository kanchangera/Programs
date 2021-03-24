# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:19:06 2021

@author: kanch
"""
num=int(input("Enter any number:"))
if num%2==0:
    print(num, " is even")
    print("Because",num, "will give yield 0 when",num,end="" "%2 is performed")
else:
    print(num, "is odd")   
    print("Because",num," will yields 1 when",num,end= "" "%2 is operated")