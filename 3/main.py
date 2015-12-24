#!/usr/bin/env python
from collections import Counter


if __name__ == '__main__':
    data = input()

    directions = {
        '^': (0, -1),
        'v': (0, +1),
        '<': (-1, 0),
        '>': (+1, 0),
    }
    location = (0, 0)

    presents = Counter()
    presents[location] += 1

    for c in data:
        location = tuple(map(sum, zip(location, directions[c])))
        presents[location] += 1

    print('{} houses received at least one present'.format(len(presents)))
