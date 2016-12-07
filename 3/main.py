#!/usr/bin/env python
import fileinput


if __name__ == '__main__':
    valid = 0
    total = 0

    for line in fileinput.input():
        lengths = sorted([int(length) for length in line.strip().split(' ') if length])

        if lengths[0] + lengths[1] > lengths[2]:
            valid += 1

        total += 1

    print('Valid Triangles: {}'.format(valid))
    print('Total Triangles: {}'.format(total))
