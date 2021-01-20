'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: takes command as input and executes it in shell
'''
from subprocess import call

try:
    command=input("enter command")
    option=input("enter option")
    call([command, option])
except OSError:
    print("invalid inputs")
