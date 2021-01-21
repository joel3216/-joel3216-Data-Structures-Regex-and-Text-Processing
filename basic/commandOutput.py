'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to print output of an external command
'''
import subprocess

try:
    command=input("enter the command")
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    print(output)
except subprocess.CalledProcessError:
    print("invalid input")