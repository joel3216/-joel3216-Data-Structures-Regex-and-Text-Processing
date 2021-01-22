'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to check whether an element exists within a tuple. 
'''

class elementExist:
    def checkElementInTuple(self,myTuple,element):
        if element in myTuple:
            return True
        return False

if __name__ == "__main__":
    try:
        myTuple=tuple(input("enter the tuple values").split(","))
        element=input("enter the element to check in tuple")
        elementCheckObj=elementExist()
        print(element," exists in ",myTuple,elementCheckObj.checkElementInTuple(myTuple,element))
    except ValueError:
        print("invalid input")