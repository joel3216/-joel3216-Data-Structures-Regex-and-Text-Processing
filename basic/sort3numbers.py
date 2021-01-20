'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION:sorts three numbers without using conditional statements 
'''
try:
    number1=int(input("enter the first number"))
    number2=int(input("enter the second number"))
    number3=int(input("enter the third number"))

    sortedNumber1=min(number1,number2,number3)
    sortedNumber3=max(number1,number2,number3)
    sortedNumber2=(number1+number2+number3)-(sortedNumber1+sortedNumber3)

    print(sortedNumber1,sortedNumber2,sortedNumber3)
except ValueError:
    print("invalid inputs")