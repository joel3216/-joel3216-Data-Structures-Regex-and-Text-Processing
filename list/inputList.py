'''
Author: Joel Jackson
Date: 21-01-2021
Description: class that contains functions to get user input for lists. 

'''
class inputList:
    def getStringInput(self):
        try:
            myList=list()
            limit=int(input("enter the number of items to add to the list"))
            if limit<0:
                raise ValueError
            for count in range(limit):
                myList.append(input("enter item no."+str(count+1)+" "))
        except ValueError:
            print("invalid input")
        else:
            return myList
    
    def getIntInput(self):
        try:
            myList=list()
            limit=int(input("enter the number of items to add to the list"))
            if limit<0:
                raise ValueError
            for count in range(limit):
                myList.append(int(input("enter item no."+str(count+1)+" ")))
        except ValueError:
            print("invalid input")
        else:
            return myList