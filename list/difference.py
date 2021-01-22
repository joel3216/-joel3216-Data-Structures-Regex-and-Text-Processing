'''
Author: Joel Jackson
Date: 21-01-2021
Description:  Python program to get the difference between the two lists.  

'''
import inputList
class listDifference:
    def getDifference(self,list1,list2):
        return list(set(list1)^set(list2))

if __name__ == "__main__":
    getInput=inputList.inputList()
    list1=getInput.getIntInput()
    list2=getInput.getIntInput()
    difference=listDifference()
    print(difference.getDifference(list1,list2))
