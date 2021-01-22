'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to calculate the length of a string.
'''
class lengthOfString:
    def printLength(self):
        string=input("enter the string")
        print(len(string))

if __name__ == "__main__":
    getLength=lengthOfString()
    getLength.printLength()