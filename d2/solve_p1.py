from fire import Fire
import operator
from typing import List


def main(test_input: List[int] = [],
         test_target: int = None):
    if not test_input:
        with open('input_1202') as f:
            input = f.read().split(',')  # have been modified accordingly
    else:
        input = test_input
    input = list(map(int, input))

    for i in range(0, len(input), 4):
        print('i', i)
        c = input[i]
        if c == 99:
            print('halt')
            break

        if c == 1:
            op = operator.add
        elif c == 2:
            op = operator.mul
        else:
            raise ValueError("Unknown operator code: %s", c)

        print('operand', input[input[i+1]], input[input[i+2]])
        input[input[i+3]] = op(input[input[i+1]], input[input[i+2]])
        print(input)

    print(input[0])
    if test_target is not None:
        print(input[0] == test_target)


if __name__ == "__main__":
    Fire(main)
