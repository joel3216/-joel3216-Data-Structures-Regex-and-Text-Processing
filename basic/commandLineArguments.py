'''
Author: Joel Jackson
Date:19-01-2021
DESCRIPTION: Program to get command line arguments 
'''
import sys

print("number of arguments: "+str(len(sys.argv))+"\nname of python file: "+str(sys.argv[0]))
if len(sys.argv) > 1:
    print("### Command Line Argumants ###")
    for item in sys.argv[1:]:
        print(item)
