from itertools import product


def get_cartesian_product(a, b):
    return list(product(a, b))


if __name__ == "__main__":
    print(get_cartesian_product([1, 2], [3, 4]))
