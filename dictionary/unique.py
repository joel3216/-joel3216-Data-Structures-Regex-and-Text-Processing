'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to print all unique values in a dictionary.  
'''

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

data=getInput() 
unique=set()
for key in data.keys():
    unique.add(data[key])
print(unique)