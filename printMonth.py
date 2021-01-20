'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION:prints calendar of given month and year 
'''
import calendar

try:
    month,year=input("enter the month and year").split(",")
    print(calendar.month(int(year),int(month)))
except ValueError:
    print("Invalid Inputs")