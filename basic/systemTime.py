'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to get the system time
'''
from datetime import datetime

time=datetime.now()
print(time.strftime("%H:%M:%S"))