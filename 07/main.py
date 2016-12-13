#!/usr/bin/env python
import fileinput


if __name__ == '__main__':
    count = 0

    for line in fileinput.input():
        line = line.strip()

        tls = False
        hypernet = False
        for i in range(0, len(line) - 3):
            if line[i] == '[':
                hypernet = True
                continue
            elif line[i] == ']':
                hypernet = False
                continue

            found = False
            if line[i + 0] != line[i + 1] and line[i + 0] == line[i + 3] and line[i + 1] == line[i + 2]:
                found = True

            if found:
                tls = True

            if hypernet and found:
                tls = False
                break

        if tls:
            count += 1

    print('TLS Supported IPs: {}'.format(count))
