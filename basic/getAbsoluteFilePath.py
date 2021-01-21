'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: gets the absolute path of file 
'''
import os

filename=input("enter the filename ") 
print("Absolute file path: ",os.path.abspath(filename))

