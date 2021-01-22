'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to search a character in the string
'''

string=input("enter the string: ")
searchString=input("enter the character to search: ")

count=0
for index in range(len(string)):
    if searchString == string[index]:
        count+=1

print(count)