from time import time
from functools import wraps


class logfile:

    def __init__(self, path):
        self.file = open(path, 'w', encoding='utf8')
    

    def __call__(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            self.file.write(str(start_time) + '\n')
            self.file.write(', '.join(list(map(str, args)) + [f"{k}={v}" for k, v in kwargs.items()]) + '\n')
            self.file.write((str(result) if result is not None else '-') + '\n')
            self.file.write(str(end_time) + '\n')
            self.file.write(str(end_time - start_time) + '\n')
            return result
        return wrapped
        


@logfile("logfile.txt")
def test_func(arg0, arg1, arg2, a=None, b=None, c=None):
    print(sum([arg0, arg1, arg2]), a, b, c)


@logfile("logfile2.txt")
def test_func2(*args):
    return args[::-1]


if __name__ == "__main__":
    test_func(1, 2, 3, a=4, b=5, c=6)
    test_func2(1, 2, 3)
