#!/usr/bin/env python
import operator
import fileinput


if __name__ == '__main__':
    directions = {
        'U': ( 0, -1),
        'D': ( 0, +1),
        'L': (-1,  0),
        'R': (+1,  0),
    }

    keypad = (
        (' ', ' ', ' ', ' ', ' ', ' ', ' '),
        (' ', ' ', ' ', '1', ' ', ' ', ' '),
        (' ', ' ', '2', '3', '4', ' ', ' '),
        (' ', '5', '6', '7', '8', '9', ' '),
        (' ', ' ', 'A', 'B', 'C', ' ', ' '),
        (' ', ' ', ' ', 'D', ' ', ' ', ' '),
        (' ', ' ', ' ', ' ', ' ', ' ', ' '),
    )

    code = []

    for line in fileinput.input():
        position = (+1, +3)
        x = 1
        y = 3

        for instr in line.strip():
            direction = directions.get(instr)

            if not direction:
                continue

            position2 = tuple(map(operator.add, position, direction))

            if keypad[position2[1]][position2[0]] == ' ':
                continue

            position = position2

        code.append(keypad[position[1]][position[0]])

    print('Bathroom code: {}'.format(''.join(code)))
