'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to find the list of words that are longer than n from a given list of words.  

'''

import inputList
class findLongWords:
    def getLongWords(self,wordList):
        try:
            size=int(input("enter the size of words to search for"))
            if size<0:
                raise ValueError
        except ValueError:
            print("invalid input")
        else:
            longWords=list()
            for word in wordList:
                if len(word)>size:
                    longWords.append(word)
            return longWords

if __name__ == "__main__":
    wordList=inputList.inputList.getStringInput(inputList)
    if wordList:
        longWords=findLongWords.getLongWords(findLongWords,wordList)
        if longWords: 
            print(longWords)