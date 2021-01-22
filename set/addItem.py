'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to add member(s) in a set. 
'''
class addItem2Set:
    def addItem(self,mySet,limit):
        for count in range(limit):
            mySet.add(int(input("enter item no."+str(count+1)+" ")))
        return mySet

if __name__ == "__main__":    
    mySet={1,2,3,4}
    try:
        limit=int(input("enter the number of items to add to the set"))
        if limit<0:
            raise ValueError
        mySet=addItem2Set.addItem(addItem2Set,mySet,limit)
    except ValueError:
        print("invalid input")
    finally:
        print(mySet)