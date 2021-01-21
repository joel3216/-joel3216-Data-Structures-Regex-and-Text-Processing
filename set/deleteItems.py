'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to remove item(s) from set  
'''

mySet={1,2,3,4}
print(mySet)
try:
    limit=int(input("enter the number of items to remove from the set"))
    if limit<0 or limit>len(mySet):
        raise ValueError
    for count in range(limit):
        mySet.remove(int(input("enter item name to delete.")))
except ValueError:
    print("invalid input")
finally:
    print(mySet)