# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:39:11 2021

@author: kanch
"""

#one line of Python that takes list a
#And makes a new list that has only the even elements of this list in it.

list1=[]
n=int(input('Enter the lenght of list'))

for i in range(n):
    x=int(input("Enter the next value:"))
    list1.append(x)
    

list2=[num for num in lst if num % 2==0]
   
print(list2)