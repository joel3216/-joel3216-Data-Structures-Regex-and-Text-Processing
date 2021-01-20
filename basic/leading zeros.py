'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to add leading zeros to a string
'''

try:
    string=input("enter the string")
    zeros=int(input("enter the number of zeros"))
    if zeros<0:
        raise ValueError
except ValueError:
    print("invalid inputs")
else:
    for count in range(zeros):
        string= '0'+string

    print(string)