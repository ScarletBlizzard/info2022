from itertools import combinations


def get_combinations(s, k):
    res = []
    for n in range(1, k+1):
        c = list(combinations(s, n))
        for i, item in enumerate(c):
            c[i] = "".join(item)
        res.extend(c)
    return res


if __name__ == "__main__":
    print(get_combinations("cat", 2))
