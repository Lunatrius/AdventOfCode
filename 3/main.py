#!/usr/bin/env python
import fileinput


if __name__ == '__main__':
    valid = 0
    total = 0

    triangles = []

    for line in fileinput.input():
        for length in line.strip().split(' '):
            if length == '':
                continue

            triangles.append(int(length))

    group_size = 9
    for group in range(0, int(len(triangles) / group_size)):
        index = group * group_size
        group_triangles = triangles[index:index+group_size]

        for i in range(0, 3):
            lengths = sorted(group_triangles[i::3])

            if lengths[0] + lengths[1] > lengths[2]:
                valid += 1

            total += 1

    print('Valid Triangles: {}'.format(valid))
    print('Total Triangles: {}'.format(total))
