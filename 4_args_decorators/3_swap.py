from functools import wraps

def swap(func):
    
    @wraps(func)
    def wrapped(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    
    return wrapped

@swap
def test_func(*args, **kwargs):
    print(*args, *kwargs)


if __name__ == "__main__":
    test_func(1, 2, 3, a=1, b=2, c=3)

