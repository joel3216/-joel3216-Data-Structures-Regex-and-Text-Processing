'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION:prints date of creation and modification time of the file 
'''
import subprocess

filepath=input("enter the file path")
print(subprocess.getoutput("ls -l "+filepath+" | awk \'{print $6\" \"$7\" \"$8}\'"))