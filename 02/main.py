#!/usr/bin/env python
import fileinput


def get_row_checksum(numbers):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] % numbers[j] == 0:
                return (numbers[i], numbers[j], int(numbers[i] / numbers[j]))

    return (None, None, None)


if __name__ == '__main__':
    checksum = 0

    for line in fileinput.input():
        line = line.strip()

        numbers = list(reversed(sorted([int(token) for token in line.split('\t')])))

        a, b, row_checksum = get_row_checksum(numbers)

        checksum += row_checksum

    print(f'Spreadsheet checksum: {checksum}')
