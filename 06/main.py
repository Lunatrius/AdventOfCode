#!/usr/bin/env python
import collections
import fileinput


if __name__ == '__main__':
    counters = []

    for line in fileinput.input():
        line = line.strip()

        while len(counters) < len(line):
            counters.append(collections.Counter())

        for i in range(0, len(line)):
            counters[i][line[i]] += 1


    message = ''.join(counter.most_common(1)[0][0] for counter in counters)
    print('Error Corrected Message: {}'.format(message))
