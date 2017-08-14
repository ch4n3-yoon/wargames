#!/usr/bin/python
# coding: utf-8
# made by ch4n3

from requests import post
import string
from bs4 import BeautifulSoup

url = 'http://burger.laboratorium.ee:8004/'
search_string = string.ascii_letters + string.digits

for character in search_string:
    data = {'query': character}
    content = post(url, data=data).content

    soup = BeautifulSoup(content, 'html.parser')
    result_list = soup.find_all('li')


    print "{0} : ".format(character),

    for result in result_list:
        for content in result.contents:
            print "{0} ".format(content.decode('utf-8')),

    print

print
print "done"
