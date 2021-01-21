'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to convert a list into a nested dictionary of keys. 
'''
mylist=input("enter the list ").split(",")
dictionary=current={}
for element in reversed(mylist):
    current[element]={}
    current=current[element]
print(dictionary)