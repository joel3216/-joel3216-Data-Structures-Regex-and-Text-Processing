'''
AUTHOR: Joel Jackson
DATE:19-01-2021
DESCRIPTION: Program to access content from a url and print it
'''
from http.client import HTTPConnection

connection=HTTPConnection("example.com")
connection.request("GET","/")
result=connection.getresponse()

print(result.read())