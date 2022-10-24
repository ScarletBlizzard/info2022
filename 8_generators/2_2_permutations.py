from itertools import permutations


def get_permutations(s, n):
    p = sorted(list(permutations(s, n)))
    for i, item in enumerate(p):
        p[i] = "".join(item)
    return p


if __name__ == "__main__":
    print(get_permutations("cat", 3))
