'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION:prints execution time of testFunction 
'''
import time

def testFunction():
    a=1+2
    print(a)

start=time.time_ns()
testFunction()
stop=time.time_ns()

print(stop-start)