'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to extract single key-value pair of a dictionary in variables.
'''
dictionary = {1 : 'one'}
(key, value), = dictionary.items()
print(key)
print(value)