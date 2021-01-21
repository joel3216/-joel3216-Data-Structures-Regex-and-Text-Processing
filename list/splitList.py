'''
Author: Joel Jackson
Date: 21-01-2021
Description:  Python program to split a list based on first character of word.

'''
from itertools import groupby
from operator import itemgetter
import inputList

class splitList:
    def splitListbyChar(self,myList):
        for letter, words in groupby(sorted(myList), key=itemgetter(0)):
            print(letter)
            for word in words:
                print(word)

if __name__ == "__main__":
    getInput=inputList.inputList()
    myList=getInput.getStringInput()
    splitListObj=splitList()
    splitListObj.splitListbyChar(myList)