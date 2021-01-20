'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to check if a variable is defined
'''
try:
  variable1 = 1
except NameError:
  print("Variable is not defined")
else:
  print("Variable is defined")

try:
  variable2
except NameError:
  print("Variable is not defined")
else:
  print("Variable is defined.")