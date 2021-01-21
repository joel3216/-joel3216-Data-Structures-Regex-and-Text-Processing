'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to add member(s) in a set. 
'''

mySet={1,2,3,4}
try:
    limit=int(input("enter the number of items to add to the set"))
    if limit<0:
        raise ValueError
    for count in range(limit):
        mySet.add(int(input("enter item no."+str(count+1)+" ")))
except ValueError:
    print("invalid input")
finally:
    print(mySet)