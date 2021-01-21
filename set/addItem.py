'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to add member(s) in a set. 
'''

mySet={1,2,3,4}
try:
    item=int(input("enter the item to add to the set"))
except ValueError:
    print("invalid input")
else:
    mySet.add(item)
    print(mySet)