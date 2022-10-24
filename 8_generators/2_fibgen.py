def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        t = a
        a += b
        b = t

if __name__ == "__main__":
    for i in fib(int(input())):
        print(i)
