'''
Author: Joel Jackson
Date: 21-01-2021
Description: Python program to find common items from two lists. 

'''
import inputList
class commonItemsCheck:
    def checkForCommonItems(self,list1,list2):
        commonItems=[]
        for item in list1:
            if item in list2:
                commonItems.append(item)
        if commonItems:
            return commonItems
        return False

if __name__ == "__main__":
    getInput=inputList.inputList()
    list1=getInput.getIntInput()
    list2=getInput.getIntInput()

    commonCheck=commonItemsCheck()
    print("Common Items: ",commonCheck.checkForCommonItems(list1,list2))