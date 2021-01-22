'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to create a dictionary from a string. 
Note: Track the count of the letters from the string.   
'''

string=input("enter the string")
characterCount={}
for character in string:
    if character not in characterCount.keys():
        characterCount[character]=1
    else:
        characterCount[character]+=1
print(characterCount)