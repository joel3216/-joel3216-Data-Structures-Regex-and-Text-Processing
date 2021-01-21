'''
Author: Joel Jackson
Date: 21-01-2021
Description: class to get user input for sets
'''
class inputSet:
    def getStringInput(self):
        try:
            mySet=set()
            limit=int(input("enter the number of items to add to the set"))
            if limit<0:
                raise ValueError
            for count in range(limit):
                mySet.add(input("enter item no."+str(count+1)+" "))
        except ValueError:
            print("invalid input")
        finally:
            return mySet
    
    def getIntInput(self):
        try:
            mySet=set()
            limit=int(input("enter the number of items to add to the set"))
            if limit<0:
                raise ValueError
            for count in range(limit):
                mySet.add(int(input("enter item no."+str(count+1)+" ")))
        except ValueError:
            print("invalid input")
        finally:
            return mySet
    