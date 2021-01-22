'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to check multiple keys exists in a dictionary.  
'''

dictionary={'one':1,'two':2,'three':3}
keycheck=input("enter the keys to check").split(",")

match=True
for item in keycheck:
    if item not in list(dictionary.keys()):
        match=False
        break

print(match)