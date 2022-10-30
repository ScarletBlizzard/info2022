def zip_(*iterables):
    iterators = [iter(i) for i in iterables]
    while True:
        try:
            yield tuple([next(i) for i in iterators])
        except StopIteration:
            return


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
