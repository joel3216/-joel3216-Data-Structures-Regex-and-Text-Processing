'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to remove duplicates from a list. 

'''
import inputList

class removeDuplicateListElements:
    def removeDuplicateItem(self,myList):
        return list(set(myList))

if __name__ == "__main__":
    myList=inputList.inputList.getIntInput(inputList)
    newList=removeDuplicateListElements.removeDuplicateItem(removeDuplicateListElements,myList)
    print(newList)