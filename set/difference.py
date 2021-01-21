'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to create set difference
'''

import inputSet

if __name__ == "__main__":
        
    set1=inputSet.inputSet.getIntInput(inputSet)
    set2=inputSet.inputSet.getIntInput(inputSet)
    difference=set1-set2
    print(difference)