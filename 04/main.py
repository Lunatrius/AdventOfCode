#!/usr/bin/env python
import fileinput


if __name__ == '__main__':
    valid = 0
    total = 0

    for line in fileinput.input():
        line = line.strip()

        tokens = line.split(' ')

        if len(set(tokens)) == len(tokens):
            valid += 1

        total += 1

    print(f'Valid passphrases: {valid} / {total}')
