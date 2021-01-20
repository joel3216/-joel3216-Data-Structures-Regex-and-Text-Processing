'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: sorts the files by date 
'''
import subprocess

print(subprocess.getoutput("ls -l  | awk \'{print $7\" \"$8\" \"$9}\' | sort"))
