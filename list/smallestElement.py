'''
Author: Joel Jackson
Date: 21-01-2021
Description: Python program to get the smallest number from a list. 

'''
import inputList
if __name__ == "__main__":
    
    myListObj=inputList.inputList()
    myList=myListObj.getIntInput()

    if(myList):
        print("Smallest element: ",min(myList))