#!/usr/bin/env python
import fileinput


if __name__ == '__main__':
    for line in fileinput.input():
        line = line.strip()

        total = 0
        for i in range(0, len(line)):
            if line[i] == line[(i + 1) % len(line)]:
                total += int(line[i])

        print(f'CAPTCHA result: {total}')
