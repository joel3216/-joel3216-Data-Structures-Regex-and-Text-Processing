'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to count number of items in a dictionary value that is a list.   
'''

dictionary={1:'one',2:[1,2,3],3:'three',4:[4,5,6]}
count=0
for item in list(dictionary.values()):
    if type(item)==list:
        count+=1
print("number of lists :"+str(count))