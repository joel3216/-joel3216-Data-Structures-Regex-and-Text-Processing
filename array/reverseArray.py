'''
Author: Joel Jackson
Date: 20-01-2021
Description: Program to reverse the order of the items in the array. 
'''
import numpy

intArray=numpy.array([1,2,3,4,5])
for index in reversed(range(len(intArray))):
    print(intArray[index])