'''
Author: Joel Jackson
Date: 20-01-2021
Description: Python program to count the values associated with key in a dictionary. 
'''
data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}] 
count=0
for dictionary in data:
    if dictionary['success']==True:
        count+=1
print(count)