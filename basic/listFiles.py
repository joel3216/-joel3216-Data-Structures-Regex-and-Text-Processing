'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to print all files in the specified directory
'''
from subprocess import call

directory=input("enter directory path")
call(["ls", "-a",directory])