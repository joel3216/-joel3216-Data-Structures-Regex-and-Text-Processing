'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to remove the first occurrence of a specified element from an array
'''
import numpy

intputArray=numpy.array( input("enter the elements for the array ").split(","))
searchKey=input("enter the element to remove ")
for index in range(len(intputArray)):
    if intputArray[index]==searchKey:
        intputArray=numpy.delete(intputArray,index)
        break

print(intputArray)