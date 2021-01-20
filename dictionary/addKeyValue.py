'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to add key,value pair to dictionary
'''
myDictionary={0: 10, 1: 20} 
try:
    key=int(input("enter the new key "))
    value=int(input("enter the new value"))
except ValueError:
    print("invalid input")
else:
    myDictionary[key]=value
    print(myDictionary)