'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: prints a histogram using the list 
'''
histogramList=[1, 9, 3, 5, 4]
for item in histogramList:
    bar=""
    for count in range(item):
        bar+='*'
    print(bar)