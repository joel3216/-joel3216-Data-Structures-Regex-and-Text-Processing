'''
Author: Joel Jackson
Date: 22-01-2021
Description:  Python program to find the repeated items of a tuple. 
'''
class repeatedTupleValues:
    def checkForRepeatedValues(self,myTuple):
        repeated=[]
        for element in myTuple:
            if myTuple.count(element)>1 and element not in repeated:
                repeated.append(element)
                print(element," repeated times: ",myTuple.count(element))

if __name__ == "__main__":
    try:
        myTuple=tuple(input("enter input values").split(","))
        repeatCheck=repeatedTupleValues()
        repeatCheck.checkForRepeatedValues(myTuple)
    except ValueError:
        print("invalid input")