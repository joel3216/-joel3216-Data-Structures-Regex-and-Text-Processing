'''
Author: Joel Jackson
Date: 21-01-2021
Description:  python program to check whether two lists are circularly identical.  

'''
import inputList
class circularCheck:
    def isCircularlyEqual(self,list1,list2):
        if len(list1)!=len(list2):
            return False
        for item in list1:
            if list1==list2:
                return True
            popped=list1.pop(0)
            list1.append(popped)
        return False

if __name__ == "__main__":
    getInput=inputList.inputList()
    list1=getInput.getIntInput()
    list2=getInput.getIntInput()
    circularCheckObj=circularCheck()
    print(circularCheckObj.isCircularlyEqual(list1,list2))