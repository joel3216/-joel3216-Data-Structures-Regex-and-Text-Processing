'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
'''

try:
    limit=int(input("enter the limit for the no of elements"))
    if limit<0:
        raise ValueError
except ValueError:
    print("invalid input")
else:
    squares={}
    for key in range(1,limit+1):
        squares[key]=key*key
    print(squares)
