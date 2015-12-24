#!/usr/bin/env python
import fileinput


def pair2(string):
    for i in range(0, len(string)):
        for j in range(i + 2, len(string)):
            if string[i:i+2] == string[j:j+2]:
                return True

    return False


def is_nice(string):
    if not pair2(string):
        return False

    if not any(1 for x in zip(string, string[2:]) if x[0] == x[1]):
        return False

    return True


if __name__ == '__main__':
    nice = len([1 for line in fileinput.input() if is_nice(line.strip())])

    print('{} strings are nice'.format(nice))
