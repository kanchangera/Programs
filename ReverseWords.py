# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:30:52 2021

@author: kanch
"""

#Rreverse words in a string


def Reverse(str):
    
    words=str.split(" ")   #['My', 'name', 'is'  'Michele']
   
    words=words[-1::-1]    #'[Michele', 'is', 'name', 'My']
    
    outputstr= ' '.join(words)   #joins them into one string
    
    print(outputstr)




string = input("Enter multi word string:")

Reverse(string)

