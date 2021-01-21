'''
Author: Joel Jackson
Date: 21-01-2021
Description: program that takes two lists and returns True if they have at least one common member.  

'''
import inputList
class commonItemCheck:
    def checkIfCommonItemExists(self,list1,list2):
        for item in list1:
            if item in list2:
                return True
        return False

if __name__ == "__main__":
    getInput=inputList.inputList()
    list1=getInput.getIntInput()
    list2=getInput.getIntInput()

    commonCheck=commonItemCheck()
    print(commonCheck.checkIfCommonItemExists(list1,list2))