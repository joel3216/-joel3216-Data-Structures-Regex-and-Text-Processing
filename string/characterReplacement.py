'''
Author: Joel Jackson
Date: 22-01-2021
Description: Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
'''

class characterReplace:
    def replacer(self):
        try:
            string=input("enter the string")
            newString=string[0]
            replace=string[0]
            replacement='$'
            for character in string[1:]:
                if character==replace:
                    newString+=replacement
                else:
                    newString+=character
            return newString
        except IndexError:
            print("invalid input")

if __name__ == "__main__":
    replaceMyString=characterReplace()
    print(replaceMyString.replacer())