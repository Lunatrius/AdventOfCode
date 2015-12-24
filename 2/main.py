#!/usr/bin/env python
import fileinput


if __name__ == '__main__':
    paper = 0

    for line in fileinput.input():
        l, w, h = dimensions = [int(i) for i in line.strip().split('x')]

        dimensions.sort()

        paper += 2 * l * w + 2 * w * h + 2 * h * l + dimensions[0] * dimensions[1]

    print('The elves should order {} square feet of wrapping paper'.format(paper))
