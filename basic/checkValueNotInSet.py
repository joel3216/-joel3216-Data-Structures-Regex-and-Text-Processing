'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION:prints elements that are mutually exclusive  
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

for element in color_list_1:
    if element not in color_list_2:
        print(element)