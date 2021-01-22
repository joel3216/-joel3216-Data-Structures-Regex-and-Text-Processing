'''
Author: Joel Jackson
Date: 21-01-2021
Description: Python program to sum all the items in a list.

'''
import inputList
if __name__ == "__main__":
    
    myListObj=inputList.inputList()
    myList=myListObj.getIntInput()

    if(myList):
        sum=0
        for number in myList:
            sum+=number
        print(sum)