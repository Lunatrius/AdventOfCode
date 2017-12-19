#!/usr/bin/env python
import fileinput


if __name__ == '__main__':
    checksum = 0

    for line in fileinput.input():
        line = line.strip()

        numbers = [int(token) for token in line.split('\t')]

        high = max(numbers)
        low = min(numbers)

        checksum += high - low

    print(f'Spreadsheet checksum: {checksum}')
