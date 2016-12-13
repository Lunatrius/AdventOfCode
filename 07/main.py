#!/usr/bin/env python
import fileinput


def is_abba(s):
    if s[0] == s[1]:
        return False

    return s[0] == s[3] and s[1] == s[2]


def check_tls(ip):
    valid = False
    subnet = False

    for i in range(0, len(ip)):
        if ip[i] == '[':
            subnet = True
            continue
        elif ip[i] == ']':
            subnet = False
            continue

        if len(ip[i:i+4]) != 4:
            continue

        if not is_abba(ip[i:i+4]):
            continue

        if subnet:
            return False

        valid = True

    return valid


if __name__ == '__main__':
    count_tls = 0

    for line in fileinput.input():
        line = line.strip()

        if check_tls(line):
            count_tls += 1

    print('TLS Supported IPs: {}'.format(count_tls))
