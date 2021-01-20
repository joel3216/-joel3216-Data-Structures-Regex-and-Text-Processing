'''
Author: Joel Jackson
Date: 20-01-2021
Description: Program to get the number of occurrences of a specified element in an array. 
'''
import numpy

intputArray=numpy.array( input("enter the elements for the array ").split(","))
searchKey=input("enter the element to search ")
count=0
for element in intputArray:
    if element==searchKey:
        count+=1

print(searchKey+" appears "+str(count)+" times in the array")
