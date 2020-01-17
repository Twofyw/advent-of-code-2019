from fastscript import *

@call_parse
def main():
    with open('input') as f:
        input = map(int, f.read().split('\n'))

    f_sum = 0
    for m in input:
        f = m // 3 - 2
        f_sum += f

    print(f_sum)