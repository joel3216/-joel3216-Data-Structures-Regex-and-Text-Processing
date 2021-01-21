'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to remove duplicates from a list of lists.

'''
class removeDuplicates:
    def removeDuplicateLists(self,data):
        unique=data.copy()
        for item in data:
            unique.remove(item)
            if item not in unique:
                unique.append(item)
        return unique

if __name__ == "__main__":
    data=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 
    removeListsObj=removeDuplicates()
    data=removeListsObj.removeDuplicateLists(data)
    print(data)