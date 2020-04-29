
from collections import Counter

def h_index(publi:list) -> int:
    c = sorted(Counter(publi).most_common())
    k, c = zip(*c)
    last_h = 0
    for i in range(len(k)):
        # print(sum(c[i:]))
        if sum(c[i:]) < last_h:
            return last_h
        last_h = sum(c[i:])

    return 0


if __name__ == "__main__":
    inputs = [1,4,1,4,2,1,3,5,6]
    print(h_index(inputs))