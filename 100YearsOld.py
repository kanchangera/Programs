# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:56:48 2021

@author: kanch
"""
#A program that asks the user to enter their name and their age.
#And tells them the year that they will turn 100 years old.

name= input('Enter your name:')
age= int(input("Enter your age:")) 

current_yr=int(input("Enter current year:"))
year=current_yr+100-age

if age>100:
   print("In", year, end="" "You have crossed 100 awesome years of your life :)")

else:
    print("In", year, end="" " you will turn 100")
   
    