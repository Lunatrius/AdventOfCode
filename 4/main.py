#!/usr/bin/env python
import re
import collections
import fileinput


if __name__ == '__main__':
    real = 0
    total = 0
    sector_sum = 0

    for line in fileinput.input():
        match = re.match(r'^(.*)-(\d+)\[([a-z0-9]+)\]$', line.strip())

        if not match:
            continue

        counter = collections.Counter(x for x in match.group(1)[::] if x != '-')
        letters = ''.join(item[0] for item in sorted(counter.most_common(), key=lambda item: (-item[1], item[0])))

        if letters[0:5] == match.group(3):
            sector_sum += int(match.group(2))
            real += 1

        total += 1

    print('Real Room Count: {}'.format(real))
    print('Total Room Count: {}'.format(total))
    print('Real Room Sector ID Sum: {}'.format(sector_sum))
