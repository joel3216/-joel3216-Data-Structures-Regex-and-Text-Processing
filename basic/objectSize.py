'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to find the available built in modules 
'''
import sys

stringObject=input("enter some input...")
print("size of "+stringObject+" in bytes: "+str(sys.getsizeof(stringObject)))