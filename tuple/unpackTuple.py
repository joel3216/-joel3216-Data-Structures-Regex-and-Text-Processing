'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to unpack a tuple in several variables.
'''

if __name__ == "__main__":
    try:
        myTuple=(1,2,3)
        element1,element2,element3=myTuple
        print(element1,element2,element3)
    except ValueError:
        print("invalid input")