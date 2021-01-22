'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to append a list to the second list.  

'''
import inputList

if __name__ == "__main__":
    getInput=inputList.inputList()
    list1=getInput.getIntInput()
    list2=getInput.getIntInput()
    list2.extend(list1)
    print(list2)