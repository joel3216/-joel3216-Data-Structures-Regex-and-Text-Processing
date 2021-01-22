'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION:concatenates elements of list into string and prints the string 
'''
inputList=input("enter the list").split(",")
concatenate=""
for element in inputList:
    concatenate+=element

print(concatenate)