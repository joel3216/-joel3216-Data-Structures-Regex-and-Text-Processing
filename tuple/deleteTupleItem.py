'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to remove an item from tuple. 
'''
class removeTupleItem:
    def getInput(self):
        try:
            myList=list()
            limit=int(input("enter the number of items to add to the tuple"))
            if limit<0:
                raise ValueError
            for count in range(limit):
                myList.append(int(input("enter item no."+str(count+1)+" ")))
            return tuple(myList)
        except ValueError:
            print("invalid input")
            return []
    
    def removeItem(self,myTuple,element):
        convertedList=list(myTuple)
        convertedList.remove(element)
        return tuple(convertedList)

if __name__ == "__main__":
    try:
        deleteItemObj=removeTupleItem()
        mytuple=deleteItemObj.getInput()
        element=int(input("enter the element to delete"))
        newtuple=deleteItemObj.removeItem(mytuple,element)
        print(type(newtuple),newtuple)
    except ValueError:
        print("please try again with proper inputs")
