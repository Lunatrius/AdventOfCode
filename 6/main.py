#!/usr/bin/env python
import fileinput
import re


if __name__ == '__main__':
    width, height = 1000, 1000
    lights = [0] * width * height

    for line in fileinput.input():
        match = re.search(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)

        action, x0, y0, x1, y1 = match.groups()

        x0 = int(x0)
        y0 = int(y0)
        x1 = int(x1)
        y1 = int(y1)

        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if action == 'turn on':
                    lights[y * width + x] += 1

                if action == 'turn off':
                    lights[y * width + x] = max(0, lights[y * width + x] - 1)

                if action == 'toggle':
                    lights[y * width + x] += 2

    brightness = sum(lights)

    print('The total brightness is {}'.format(brightness))
