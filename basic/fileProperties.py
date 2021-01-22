'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to print file properties
'''
import os
import time

try:
    filename=input("enter the filename")
    print('last access time :', time.ctime(os.path.getatime(filename)))
    print('last modified time :', time.ctime(os.path.getmtime(filename)))
    print('size :', os.path.getsize(filename))
except FileNotFoundError:
    print("invalid input")