# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:22:35 2021

@author: kanch
"""


"""A program (function!) that takes a list 
And returns a new list that contains all the elements of the first list
minus all the duplicates."""

def RemoveDup(mylist):       #mylist as argument

    final_list = []          #creates new list

    for num in mylist:

        if num not in final_list:   #checks for the unique numbers

            final_list.append(num)

    return final_list              #return list without duplicacy


mylist=[]

x=int(input('Enter number of elements in list:'))

for i in range(x):                   #tales list elements upto n
    
    print('Enter',i+1,end=" " 'value:')
    
    x=int(input())
    
    mylist.append(x)

print(mylist) 


print(RemoveDup(mylist))     #calling RemoveDup function inside print method


#you can also use set() to remove duplicacy
#z=set(list)
#list=list(z)
#print(z)
          