from itertools import groupby


def compress_string(s):
    return [(len(list(g)), int(k)) for k, g in groupby(s)]


if __name__ == "__main__":
    print(compress_string('1222311'))
