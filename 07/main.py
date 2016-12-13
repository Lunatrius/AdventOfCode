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


def is_aba(s):
    if s[0] == s[1]:
        return False

    return s[0] == s[2]


def has_bab(ip, ch1, ch2):
    subnet = False

    for i in range(0, len(ip)):
        if ip[i] == '[':
            subnet = True
            continue
        elif ip[i] == ']':
            subnet = False
            continue

        if not subnet:
            continue

        if ip[i:i+3] == ch2 + ch1 + ch2:
            return True

    return False


def check_ssl(ip):
    subnet = False

    for i in range(0, len(ip)):
        if ip[i] == '[':
            subnet = True
            continue
        elif ip[i] == ']':
            subnet = False
            continue

        if subnet:
            continue

        if len(ip[i:i+3]) != 3:
            continue

        if not is_aba(ip[i:i+3]):
            continue

        if has_bab(ip, ip[i + 0], ip[i + 1]):
            return True

    return False


if __name__ == '__main__':
    count_tls = 0
    count_ssl = 0

    for line in fileinput.input():
        line = line.strip()

        if check_tls(line):
            count_tls += 1

        if check_ssl(line):
            count_ssl += 1

    print('TLS Supported IPs: {}'.format(count_tls))
    print('SSL Supported IPs: {}'.format(count_ssl))
