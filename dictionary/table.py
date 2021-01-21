'''
Author: Joel Jackson
Date: 20-01-2021
Description: program to print a dictionary as a table
'''
table={'row1':[1,2,3],'row2':[4,5,6],'row3':[7,8,9]}

for key in table.keys():
    print(key+":\t{}\t{}\t{}".format(table[key][0],table[key][1],table[key][2]))
