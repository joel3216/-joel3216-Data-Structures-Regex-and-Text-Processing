'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to convert a list into a nested dictionary of keys. 
'''

if __name__ == "__main__":
    
    mylist=input("enter the list ").split(",")
    dictionary=current={}
    for element in mylist:
        value=input("enter the value")
        current[element]=value,{}
        current=current[element][1]
    print(dictionary)