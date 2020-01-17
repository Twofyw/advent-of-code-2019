from fire import Fire

INPUT_RANGE = range(248345, 746315+1)

def validate(x: int) -> bool:
    s = str(x)
    for b, c in zip(s[:-1], s[1:]):
        if b > c: return False

    if s[0] == s[1] and s[1] != s[2]: return True
    if s[-1] == s[-2] and s[-2] != s[-3]: return True
    for i in range(3):
        if s[1+i] == s[2+i] and s[i] != s[1+i] and s[2+i] != s[3+i]:
            return True
    return False


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
