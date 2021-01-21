'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: prints number of days between two dates
'''
from datetime import date

def getDate():
    try:
        year,month,day=input("enter year,month,day ").split(",")
        return int(year),int(month),int(day)
    except ValueError:
        print("Invalid Input")
    except TypeError:
        print("Invalid Input")

try:
    print("enter the first date")
    year1,month1,day1=getDate()

    print("enter the second date")
    year2,month2,day2=getDate()

    firstDate=date(year1,month1,day1)
    secondDate=date(year2,month2,day2)

    difference=secondDate-firstDate
    print(difference.days)
except TypeError:
    pass
