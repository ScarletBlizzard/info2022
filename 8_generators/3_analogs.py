def zip_(*iterables):
    i = 0
    while True:
        try:
            yield tuple(iterable[i] for iterable in iterables)
            i += 1
        except IndexError:
            break


def map_(func, iterable):
    for item in iterable:
        yield func(item)


def enumerate_(iterable, start=0):
    i = start
    for item in iterable:
        yield i, item
        i += 1


if __name__ == "__main__":
    for i, j in zip_([-1,2,-3],[9,-8,7,6,5,4]):
        print(i,j)
    print(list(map_(max, [[2,1],[0,1]])))
