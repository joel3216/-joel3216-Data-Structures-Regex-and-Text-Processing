'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to slice a tuple.. 
'''

class tupleSlice:
    def slicer(self,myTuple,index1,index2):
        return myTuple[index1:index2]

if __name__ == "__main__":
    try:
        myTuple=tuple(input("enter input values").split(","))
        index1=int(input("enter first index"))
        index2=int(input("enter second index"))

        sliceObj=tupleSlice()
        myTuple=sliceObj.slicer(myTuple,index1,index2)
        print(type(myTuple),myTuple)
    except ValueError:
        print("invalid input")
