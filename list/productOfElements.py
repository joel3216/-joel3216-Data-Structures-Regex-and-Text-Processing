'''
Author: Joel Jackson
Date: 21-01-2021
Description: Python program to product all the items in a list.

'''

import inputList
if __name__ == "__main__":
    
    myListObj=inputList.inputList()
    myList=myListObj.getIntInput()

    if(myList):
        product=1
        for number in myList:
            product*=number
        print(product)