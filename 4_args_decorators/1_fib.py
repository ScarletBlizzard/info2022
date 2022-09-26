import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int)
    parser.add_argument('number', nargs='?', type=int)

    return parser


memory = {1: 0, 2: 1}
def fib(N):
    if N in memory:
        return memory[N]
    memory[N] = fib(N-1) + fib(N-2)
    return memory[N]


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        sys.exit("error: exactly 1 argument is required")

    parser = createParser()
    args = parser.parse_args()

    N = args.n
    if N is None:
        N = args.number

    print(fib(N))
