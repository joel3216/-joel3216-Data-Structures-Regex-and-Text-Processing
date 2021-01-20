'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: checks if a number is in the given list 
'''

try:
    testData=input("enter the list").split(",")
    for index in range(len(testData)):
        testData[index]=int(testData[index])
    check=int(input("enter the number to check if its in the list"))

    print(check in testData)
except ValueError:
    print("invalid inputs")
except TypeError:
    print("invalid inputs")
