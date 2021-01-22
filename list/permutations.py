'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to generate all permutations of a list in Python.  

'''
import inputList
from itertools import permutations

if __name__ == "__main__":
    getInput=inputList.inputList()
    myList=getInput.getIntInput()
    listPermutations=list(permutations(myList))
    print(listPermutations)
    