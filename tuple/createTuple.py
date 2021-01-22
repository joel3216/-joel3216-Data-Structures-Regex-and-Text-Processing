'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to create a tuple.
'''

if __name__ == "__main__":
    try:
        myTuple=tuple(input("enter input values").split(","))
        print(type(myTuple),myTuple)
    except ValueError:
        print("invalid input")