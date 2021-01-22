'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to find minimum and maximum in set. 

'''

import inputSet

if __name__ == "__main__":
        
    mySet=inputSet.inputSet.getIntInput(inputSet)
    print("minimum: "+str(min(mySet)))
    print("maximum: "+str(max(mySet)))