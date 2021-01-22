'''
Author: Joel Jackson
Date: 21-01-2021
Description: Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 

'''
import inputList
class stringListOperations:
    def lengthCountCheck(self,element):
        if len(element)>=2:
            return True
    
    def firstAndLastCharacterCheck(self,element):
        if element[0]==element[-1]:
            return True


if __name__ == "__main__":
    try:
        getUserInput = inputList.inputList()
        myList=getUserInput.getStringInput()
        stringListObj=stringListOperations()
        count=0
        for element in myList:
            if stringListObj.lengthCountCheck(element) and stringListObj.firstAndLastCharacterCheck(element):
                count+=1
        print(count)
    except TypeError:
        print("Please try again with the proper input")

    