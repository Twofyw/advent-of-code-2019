from fire import Fire
import numpy as np
from typing import List
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

@dataclass
class Line:
    p1: Point
    p2: Point


def path_to_coord(path):
    path = path.split(',')
    curr, coords = np.array([0, 0]), []
    for p in path:
        dir = p[0]
        dist = int(p[1:])
        if dir == 'U':
            unit = np.array([0, 1])
        if dir == 'D':
            unit = np.array([0, -1])
        if dir == 'L':
            unit = np.array([-1, 0])
        if dir == 'R':
            unit = np.array([1, 0])
        end = curr + dist * unit
        coords.append((curr, end))
        curr = end
    return coords


def length(line):
    (x1, y1), (x2, y2) = line
    return abs(x1 - x2) + abs(y1 - y2)


def intersect(coords1, coords2):
    """

    :param coords1: [(np.array((x1, y1)), np.array((x2, y2))), (...)]
    :param coords2:
    :return:
    """
    intersects = []
    for i1, l1 in enumerate(coords1):
        for i2, l2 in enumerate(coords2):
            (x11, y11), (x12, y12) = l1
            (x21, y21), (x22, y22) = l2
            parallel = ((x11 == x12) == (x21 == x22))
            if not parallel:
                if x11 == x12:
                    perp = l1
                    horiz = l2
                else:
                    perp = l2
                    horiz = l1
                (x11, y11), (x12, y12) = perp
                (x21, y21), (x22, y22) = horiz
                if (x11 >= min(x21, x22)) and (x11 <= max(x21, x22)) \
                        and (y21 >= min(y11, y12)) and (y21 <= max(y11, y12)):
                    x_cross, y_cross = x11, y21
                    steps = 0
                    for past in coords1[:i1]:
                        steps += length(past)
                    for past in coords2[:i2]:
                        steps += length(past)
                    steps += abs(x_cross - x11) + abs(y_cross - y11) + abs(x_cross - x21) + abs(y_cross - y21)
                    intersects.append((steps, x_cross, y_cross))
    return intersects


def min_steps(intersects):
    return min(o[0] for o in intersects[1:])


def main(test_input: List[int] = [],
         test_target: int = None):
    if not test_input:
        with open('input') as f:
            input = f.read()  # have been modified accordingly
    else:
        input = test_input
    paths = input.split('\n')
    coords1, coords2 = (path_to_coord(p) for p in paths)
    print(coords1, coords2)
    interceptions = intersect(coords1, coords2)
    print('interceptions', interceptions)
    print(min_steps(interceptions))


if __name__ == "__main__":
    Fire(main)
