'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to sort dictionary by value
'''
from operator import itemgetter
def getInput():
    try:
        dictionaryInput={}
        limit=int(input("enter the limit of the dictionary"))
        for count in range(limit):
            key=input("enter the key")
            dictionaryInput[key]=int(input("enter the input for key: "+key))
    except ValueError:
        print("invalid input")
    finally:
        return dictionaryInput



myDictionary=getInput()
if myDictionary:
    ascendingList=sorted(myDictionary.items(),key=itemgetter(1))
    descendingList=sorted(myDictionary.items(),key=itemgetter(1),reverse=True)
    print("Ascending Order: "+str(ascendingList))
    print("Descending Order: "+str(descendingList))
    


