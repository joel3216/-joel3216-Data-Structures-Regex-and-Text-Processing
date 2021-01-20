'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: checks if the specified file exist or not 
'''
import os.path
from os import path

filePath=input("enter the path to file")
print(str(path.exists(filePath)))