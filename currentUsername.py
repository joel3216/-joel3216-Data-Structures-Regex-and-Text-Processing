'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: prints the username 
'''
import subprocess

print(subprocess.getoutput("env | grep USERNAME"))