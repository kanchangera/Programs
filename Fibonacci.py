# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:00:25 2021

@author: kanch
"""

def fibo(n):
    
    a=0
    
    b=1

    if n<0:
        print("Please enter positive number:")
    
    elif n==0:
            
            print(a)
        
    else:
        print(a)
            
        print(b)
            
        for i in range(2,n):
            
            c=a+b
                
            a=b
                
            b=c
                
            print(c)
            
x= int(input('How many Fibonnaci numbers to generate:'))

result= fibo(x)
