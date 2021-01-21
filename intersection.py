'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to create an intersection of sets. 
'''
set1={1,2,3,4,5}
set2={1,3,5}
intersection=set()

for element in set1:
    if element in set2:
        intersection.add(element)
print(intersection)