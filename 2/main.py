#!/usr/bin/env python
import fileinput


def clamp(value, _min, _max):
    if value < _min:
        return _min

    if value > _max:
        return _max

    return value

if __name__ == '__main__':
    keypad = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    )

    code = []

    for line in fileinput.input():
        x = 1
        y = 1

        for instr in line.strip():
            if instr == 'U':
                y = clamp(y - 1, 0, 2)
            elif instr == 'D':
                y = clamp(y + 1, 0, 2)
            elif instr == 'L':
                x = clamp(x - 1, 0, 2)
            elif instr == 'R':
                x = clamp(x + 1, 0, 2)

        code.append(str(keypad[y][x]))

    print('Bathroom code: {}'.format(''.join(code)))
