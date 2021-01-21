'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to get the host name
'''
import subprocess

print(subprocess.getoutput("env | grep HOSTNAME"))