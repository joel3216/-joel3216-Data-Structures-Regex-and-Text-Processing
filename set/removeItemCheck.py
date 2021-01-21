'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to remove an item from a set if it is present in the set.
'''
def getInput():
    try:
        mySet=set()
        limit=int(input("enter the number of items to add to the set"))
        if limit<0:
            raise ValueError
        for count in range(limit):
            mySet.add(int(input("enter item no."+str(count+1)+" ")))
    except ValueError:
        print("invalid input")
    finally:
        return mySet

mySet=getInput()
try:
    element=int(input("enter the element to delete"))
    if element in mySet:
        mySet.remove(element)
    else:
        raise ValueError
except ValueError:
    print("invalid input")
finally:
    print(mySet)
