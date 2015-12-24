#!/usr/bin/env python

if __name__ == '__main__':
    data = input()
    floor = 0
    down = None

    for i, c in enumerate(data):
        floor += +1 if c == '(' else -1

        if down is None and floor == -1:
            down = i + 1

    print('Santa entered the basement at {}'.format(down))
    print('Santa is on floor {}'.format(floor))
