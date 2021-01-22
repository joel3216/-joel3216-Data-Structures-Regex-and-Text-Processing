'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to remove an item from a set if it is present in the set.
'''
import inputSet

class removeListItem:
    def removeItem(self):
        element=int(input("enter the element to delete"))
        if element in mySet:
            mySet.remove(element)
        else:
            raise ValueError
        return mySet

mySet=inputSet.inputSet.getIntInput(inputSet)
try:
    mySet=removeListItem.removeItem(removeListItem)
except ValueError:
    print("invalid input")
else:
    print(mySet)
