#!/usr/bin/env python
import operator


if __name__ == '__main__':
    directions = (
        ( 0, -1),
        (+1,  0),
        ( 0, +1),
        (-1,  0),
    )

    data = input()
    index = 0
    position = ( 0,  0)

    for instruction in data.split(', '):
        if instruction[0:1] == 'R':
            index = (index + 1) % len(directions)
        elif instruction[0:1] == 'L':
            index = (index - 1) % len(directions)
        else:
            raise Exception('invalid rotation')

        length = int(instruction[1:])
        direction = tuple(length * i for i in directions[index])
        position = tuple(map(operator.add, position, direction))

        print('{:5} | {:15} | {:15}'.format(instruction, str(direction), str(position)))

    print('Easter Bunny HQ Position: {}'.format(position))
    print('Easter Bunny HQ Distance: {}'.format(sum(abs(i) for i in position)))
