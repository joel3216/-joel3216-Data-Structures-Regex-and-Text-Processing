'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: program to accept values into list and tuple and print it 
'''
try:
    listInput=input("enter comma separated vaules").split(",")
    for index in range(len(listInput)):
        listInput[index]=int(listInput[index])
    tupleInput=tuple(listInput)
    print("list: ",listInput)
    print("tuple: ",tupleInput)
except TypeError:
    print("invalid inputs")
except ValueError:
    print("invalid inputs")