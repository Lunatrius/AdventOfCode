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
    positions = []
    duplicates = []

    for instruction in data.split(', '):
        if instruction[0:1] == 'R':
            index = (index + 1) % len(directions)
        elif instruction[0:1] == 'L':
            index = (index - 1) % len(directions)
        else:
            raise Exception('invalid rotation')

        length = int(instruction[1:])
        for _ in range(0, length):
            position = tuple(map(operator.add, position, directions[index]))

            if position in positions:
                duplicates.append(position)
            else:
                positions.append(position)

        print('{:5} | {:15}'.format(instruction, str(position)))

    print('Easter Bunny HQ Position: {}'.format(position))
    print('Easter Bunny HQ Distance: {}'.format(sum(abs(i) for i in position)))
    print('Actual Easter Bunny HQ Position: {}'.format(duplicates[0]))
    print('Actual Easter Bunny HQ Distance: {}'.format(sum(abs(i) for i in duplicates[0])))
