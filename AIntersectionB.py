# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:19:37 2021

@author: kanch
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = set(a)

b = set(b)

x = a.intersection(b)

print(x)
