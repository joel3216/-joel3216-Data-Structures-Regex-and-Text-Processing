'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to determine if the python shell is executing in 32bit or 64bit mode on operating system.
'''
import struct
print(struct.calcsize("P") * 8)