#!/usr/bin/env python
import hashlib


if __name__ == '__main__':
    data = input()
    i = 1

    while hashlib.md5(('{}{}'.format(data, i)).encode('utf-8')).hexdigest()[:5] != '0' * 5:
        i += 1

    print('The AdventCoin is at {}'.format(i))
