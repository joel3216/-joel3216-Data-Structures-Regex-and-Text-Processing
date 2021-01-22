'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to convert a list into a tuple. 
'''

class list2tuple:
    def getList2tuple(self):
        try:
            myList=list()
            limit=int(input("enter the number of items to add to the list"))
            if limit<0:
                raise ValueError
            for count in range(limit):
                myList.append(int(input("enter item no."+str(count+1)+" ")))
            return tuple(myList)
        except ValueError:
            print("invalid input")
            return []

if __name__ == "__main__":
    convertObj=list2tuple()
    mytuple=convertObj.getList2tuple()
    print(type(mytuple),mytuple)
            