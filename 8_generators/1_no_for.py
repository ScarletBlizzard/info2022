def print_map(function, iterable):
    while True:
        try:
            print(function(next(iterable)))
        except StopIteration:
            return

if __name__ == "__main__":
    print_map(lambda x: x*x, iter(range(1,6)))
