'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to to clone or copy a list. 

'''
import inputList

if __name__ == "__main__":
    
    list1=inputList.inputList.getIntInput(inputList)
    list2=list1.copy()
    print("list 2: ",list2)
