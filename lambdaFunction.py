'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to get numbers divisible by fifteen from a list using an anonymous function
'''
try:
    listInput=input("enter list").split(",")
    for index in range(len(listInput)):
        listInput[index]=int(listInput[index])

    result = list(filter(lambda x: (x % 15 == 0), listInput))
    print("Numbers divisible by 15 are: ",result)
except ValueError:
    print("invalid inputs")