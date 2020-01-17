from fire import Fire
import operator
from typing import List

def solve(memory):
    input = memory
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

    return input[0]

def main(test_input: List[int] = [],
         test_target: int = None):
    if not test_input:
        with open('input_raw') as f:
            input = f.read().split(',')  # have been modified accordingly
    else:
        input = test_input
    for noun in range(100):
        for verb in range(100):
            print(f'noun: {noun}, verb: {verb}')
            memory = list(map(int, input))
            memory[1:3] = [noun, verb]
            output = solve(memory)
            if output == 19690720:
                print('submit', 100 * noun + verb)
                return 0


if __name__ == "__main__":
    Fire(main)
