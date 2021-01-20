'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to convert an integer to binary keep leading zeros.
'''
try:
    number=int(input("enter the integer"))
except ValueError:
    print("invalid input")
else:
    print(format(number, '08b'))