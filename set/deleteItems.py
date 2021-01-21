'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to remove item(s) from set  
'''
class deleteListItem:
    def deleteItem(self,mySet):
        limit=int(input("enter the number of items to remove from the set"))
        if limit<0 or limit>len(mySet):
            raise ValueError
        for count in range(limit):
            mySet.remove(int(input("enter item name to delete.")))
        return mySet

if __name__ == "__main__":
    
    mySet={1,2,3,4}
    print(mySet)
    try:
        mySet=deleteListItem.deleteItem(deleteListItem,mySet)
    except ValueError:
        print("invalid input")
    except KeyError:
        print("entered item was not in set")
    finally:
        print(mySet)