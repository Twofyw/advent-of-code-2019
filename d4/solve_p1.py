from fire import Fire

INPUT_RANGE = range(248345, 746315+1)

def validate(x: int) -> bool:
    s = str(x)
    last_adj = None
    for a, b in zip(s[:-1], s[1:]):
        if a > b: return False
        if a == b:

    return


def main(test_input: str = '',
         test_target: int = None):
    # if not test_input:
    #     with open('input') as f:
    #         input = f.read()  # have been modified accordingly
    # else:
    #     input = test_input
    valids = [x for x in INPUT_RANGE if validate(x)]
    print(valids)
    print(len(valids))


if __name__ == "__main__":
    Fire(main)
