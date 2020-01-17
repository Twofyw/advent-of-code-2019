from fire import Fire
import numpy as np
from typing import List

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


def intersect(coords1, coords2):
    """

    :param coords1: [(np.array((x1, y1)), np.array((x2, y2))), (...)]
    :param coords2:
    :return:
    """
    intersects = []
    for l1 in coords1:
        for l2 in coords2:
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
                    intersects.append((x11, y21))
    return intersects


def closest(interceptions):
    dist = (abs(o[0]) + abs(o[1]) for o in interceptions)
    return min((o for o in dist if o))


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
    print(closest(interceptions))


if __name__ == "__main__":
    Fire(main)
