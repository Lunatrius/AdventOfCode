#!/usr/bin/env python

if __name__ == '__main__':
    data = input()
    floor = 0

    for c in data:
        floor += +1 if c == '(' else -1

    print('Santa is on floor {}'.format(floor))
