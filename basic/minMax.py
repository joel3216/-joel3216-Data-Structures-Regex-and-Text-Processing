'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to find the maximum and minimum numbers from a sequence of numbers. 
'''
def findMin(inputList):
    minimum=inputList[0]
    for element in inputList[1:]:
        if minimum>element:
            minimum=element
    return minimum

def findMax(inputList):
    maximum=inputList[0]
    for element in inputList[1:]:
        if maximum<element:
            maximum=element
    return maximum

inputList=input("enter the list ").split(",")
for key in range(len(inputList)):
    inputList[key]=int(inputList[key])

print("minimum: ",findMin(inputList),"\nmaximum: ",findMax(inputList))
