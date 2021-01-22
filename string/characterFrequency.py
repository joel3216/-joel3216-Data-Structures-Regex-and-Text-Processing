'''
Author: Joel Jackson
Date: 22-01-2021
Description: program to count the number of characters (character frequency) in a string.
'''
class getFrequency:
    def charFrequency(self,string):
        frequency={}
        for character in string:
            if character in frequency.keys():
                frequency[character]+=1
            else:
                frequency[character]=1
        return frequency

string=input("input the string ")
characterCount=getFrequency()
print(characterCount.charFrequency(string))