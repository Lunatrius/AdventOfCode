#!/usr/bin/env python
import sys
import hashlib


if __name__ == '__main__':
    door_id = input()

    password = [None,] * 8
    found = 0
    index = 0

    common_hash = hashlib.md5()
    common_hash.update(bytes(door_id, 'utf-8'))

    while found < 8:
        door_hash = common_hash.copy()
        door_hash.update(bytes(str(index), 'utf-8'))

        hex_hash = door_hash.hexdigest()

        if hex_hash[0:5] == '00000':
            i = ord(hex_hash[5]) - ord('0')
            if i < 0 or i >= len(password):
                index += 1
                continue

            if password[i]:
                index += 1
                continue

            found += 1
            password[i] = hex_hash[6]

        if index % 100000 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()

        index += 1

    print('')

    password = ''.join(password)

    print('Door ID: {}'.format(door_id))
    print('Iterations: {}'.format(index))
    print('The Password: {}'.format(password))
