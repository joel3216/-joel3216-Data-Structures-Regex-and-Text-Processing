'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to reverse a tuple.
'''

if __name__ == "__main__":
    try:
        myTuple=tuple(input("enter input values").split(","))
        reverseTuple=tuple(reversed(myTuple))
        print(type(reverseTuple),reverseTuple)
    except ValueError:
        print("invalid input")