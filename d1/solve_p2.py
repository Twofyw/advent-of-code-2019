from fire import Fire
from typing import List

def calculate_fuel_including_itself(mass):
    total = 0
    fuel = mass
    while fuel > 0:
        fuel = calculate_fuel(fuel)
        if fuel > 0: total += fuel
    return total

def calculate_fuel(mass):
    return mass // 3 - 2

def main(test_input: List[int] = [],
         test_target: int = None):
    if not test_input:
        with open('../d2/input_1202') as f:
            input = map(int, f.read().split('\n'))
    else:
        input = test_input

    f_sum = 0
    for m in input:
        f = calculate_fuel_including_itself(m)
        f_sum += f

    print(f_sum)
    if test_target is not None:
        print(f_sum == test_target)


if __name__ == "__main__":
    Fire(main)
