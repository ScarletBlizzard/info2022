def print_map(function, iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(function(next(iterator)))
        except StopIteration:
            return

if __name__ == "__main__":
    print_map(lambda x: x*x, range(1,6))
