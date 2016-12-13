#!/usr/bin/env python
import fileinput


def rect(screen, w, h, width, height):
    for y in range(0, h):
        for x in range(0, w):
            screen[y][x] = '#'


def rotate_row(screen, y, count, width, height):
    data = []

    for x in range(0, width):
        data.append(screen[y][x])

    for x in range(0, width):
        screen[y][x] = data[(x - count) % width]


def rotate_column(screen, x, count, width, height):
    data = []

    for y in range(0, height):
        data.append(screen[y][x])

    for y in range(0, height):
        screen[y][x] = data[(y - count) % height]


if __name__ == '__main__':
    width = 50
    height = 6

    screen = [['.' for _ in range(0, width)] for _ in range(0, height)]
    for line in fileinput.input():
        line = line.strip()

        if line.startswith('rect '):
            w, h = line[5:].split('x')
            rect(screen, int(w), int(h), width, height)
        elif line.startswith('rotate row y='):
            y, count = line[13:].split(' by ')
            rotate_row(screen, int(y), int(count), width, height)
        elif line.startswith('rotate column x='):
            x, count = line[16:].split(' by ')
            rotate_column(screen, int(x), int(count), width, height)
        else:
            raise Exception('invalid instruction')

    print('\n'.join(''.join(row) for row in screen))

    lit_pixels = sum(sum(1 for col in row if col == '#') for row in screen)

    print('')
    print('Lit Pixels: {}'.format(lit_pixels))
