'''
Author: Joel Jackson
Date: 21-01-2021
Description: Python program to product all the items in a list.

'''

def getInput():
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

myList=getInput()
if(myList):
    product=0
    for number in myList:
        product*=number
    print(product)