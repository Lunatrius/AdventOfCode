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
    locations = [(0, 0), (0, 0)]

    presents = Counter()
    for location in locations:
        presents[location] += 1

    for i, c in enumerate(data):
        which = i % len(locations)
        locations[which] = tuple(map(sum, zip(locations[which], directions[c])))
        presents[locations[which]] += 1

    print('{} houses received at least one present'.format(len(presents)))
