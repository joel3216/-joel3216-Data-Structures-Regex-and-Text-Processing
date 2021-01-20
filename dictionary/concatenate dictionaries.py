'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to concatenate dictionaries
'''

def concatenateDictionaries(sumDictionary,dictionary):
    for key in dictionary.keys():
        sumDictionary[key]=dictionary[key]
    return sumDictionary

dictionary1={1:10, 2:20} 
dictionary2={3:30, 4:40} 
dictionary3={5:50,6:60}

dictionary1=concatenateDictionaries(dictionary1,dictionary2)
dictionary1=concatenateDictionaries(dictionary1,dictionary3)
print(dictionary1)
