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

        encrypted_name = match.group(1)
        sector_id = int(match.group(2))
        checksum = match.group(3)

        counter = collections.Counter(x for x in encrypted_name[::] if x != '-')
        letters = ''.join(item[0] for item in sorted(counter.most_common(), key=lambda item: (-item[1], item[0])))

        if letters[0:5] == checksum:
            sector_sum += int(sector_id)
            real += 1

            start = ord('a')
            characters = []
            for ch in encrypted_name:
                if ch == '-':
                    characters.append(' ')
                else:
                    characters.append(chr((ord(ch) - start + int(sector_id)) % 26 + start))

            name = ''.join(characters)

            if 'northpole object' in name:
                print('Found "{}" in sector {} ({})'.format('northpole object', sector_id, name))

        total += 1

    print('Real Room Count: {}'.format(real))
    print('Total Room Count: {}'.format(total))
    print('Real Room Sector ID Sum: {}'.format(sector_sum))
