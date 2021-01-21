'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: gets the syntax and description of the built-in function 
'''
try:
    function=input("enter the built-in python function")
    help(function)
except NameError:
    print("Invalid input")