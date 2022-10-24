from itertools import combinations_with_replacement

def get_combinations_with_r(s, n):
    c = list(combinations_with_replacement(s, n))
    for i, item in enumerate(c):
        c[i] = "".join(item)
    return c


if __name__ == "__main__":
    print(get_combinations_with_r("cat", 2))
