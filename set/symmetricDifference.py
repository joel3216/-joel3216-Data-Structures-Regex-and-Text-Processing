'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to create a symmetric difference. 

'''

def getInput():
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
    
set1=getInput()
set2=getInput()
difference=set1^set2
print(difference)