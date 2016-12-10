#!/usr/bin/env python
import sys
import hashlib


if __name__ == '__main__':
    door_id = input()

    password = []
    index = 0

    common_hash = hashlib.md5()
    common_hash.update(bytes(door_id, 'utf-8'))

    while len(password) < 8:
        door_hash = common_hash.copy()
        door_hash.update(bytes(str(index), 'utf-8'))

        hex_hash = door_hash.hexdigest()

        if hex_hash[0:5] == '00000':
            password.append(hex_hash[5])

        if index % 100000 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()

        index += 1

    print('')

    password = ''.join(password)

    print('Door ID: {}'.format(door_id))
    print('Iterations: {}'.format(index))
    print('The Password: {}'.format(password))
