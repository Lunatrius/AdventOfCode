#!/usr/bin/env python
import math
import operator
import fileinput


def get_grid(size):
    position = (0, 0)
    x = 0
    y = 0

    directions = [
        ( 0, +1),
        (+1,  0),
        ( 0, -1),
        (-1,  0),
    ]

    steps_max = 0
    steps_cur = 0
    index = 0

    for i in range(0, size):
        yield position

        if steps_cur >= steps_max:
            steps_cur = 0

            if index % 2 == 0:
                steps_max += 1

            index = (index + 1) % len(directions)

        steps_cur += 1

        direction = directions[index]
        position = tuple(map(operator.add, position, direction))


if __name__ == '__main__':
    for line in fileinput.input():
        line = line.strip()

        position = int(line)
        grid = list(get_grid(position))

        x, y = grid[-1]
        steps = abs(x) + abs(y)

        print(f'Location: {x} {y}')
        print(f'Steps to access port: {steps}')

        data = {
            (0, 0): 1
        }

        for pos in grid:
            if pos in data:
                continue

            total = 0

            for y in range(-1, 2):
                for x in range(-1, 2):
                    if x == 0 and y == 0:
                        continue

                    rpos = tuple(map(operator.add, pos, (x, y)))
                    total += data.get(rpos, 0)

            data[pos] = total

            if total > position:
                print(f'First larger value: {total}')
                break
