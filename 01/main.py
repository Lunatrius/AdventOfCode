#!/usr/bin/env python
import fileinput


if __name__ == '__main__':
    for line in fileinput.input():
        line = line.strip()

        total = 0
        for i in range(0, len(line)):
            j = (i + int(len(line) / 2)) % len(line)
            if line[i] == line[j]:
                total += int(line[i])

        print(f'CAPTCHA result: {total}')
