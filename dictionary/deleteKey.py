'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to remove a key from a dictionary. 
'''

dictionary={1:10,2:20,3:30,4:40}
try:
    key=int(input("enter the key to delete"))
    if key not in dictionary.keys():
        raise ValueError
except ValueError:
    print("invalid input")
else:
    del dictionary[key]
    print(dictionary)