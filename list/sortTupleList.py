'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

'''
from operator import itemgetter
class sortTupleList:
    data=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
    def sortTupleByValue(self):
        sortedList=sorted(self.data,key=itemgetter(1))
        return sortedList

if __name__ == "__main__":
    sortedList=sortTupleList.sortTupleByValue(sortTupleList)
    print(sortedList)