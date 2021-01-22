'''
Author: Joel Jackson
Date: 21-01-2021
Description: program to print a specified list after removing the 0th, 4th and 5th elements.  

'''
if __name__ == "__main__":
    data=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
    data.pop(0)
    data.pop(-3)
    data.pop(-2)
    print(data)