#!/usr/bin/env python
import fileinput


def is_nice(string):
    if sum(string.count(c) for c in 'aeiou') < 3:
        return False

    if not any(1 for x in zip(string, string[1:]) if x[0] == x[1]):
        return False

    if any(s in string for s in ['ab', 'cd', 'pq', 'xy']):
        return False

    return True


if __name__ == '__main__':
    nice = len([1 for line in fileinput.input() if is_nice(line.strip())])

    print('{} strings are nice'.format(nice))
