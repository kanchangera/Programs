# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 08:47:46 2021

@author: kanch
"""

#Program that tells the multiples of entered number

num=int(input('Enter number:'))

print('Divisor of ',num,'are:')

for i in range(1,num):
    if num%i==0:
        print(i,end=" ")