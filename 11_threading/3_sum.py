from time import time
from threading import Thread

sums = []

def lst_sum(lst, idx, start, end):
    global sums
    s = 0
    for i in range(start, end):
        s += lst[i]
    sums[idx] = s

if __name__ == "__main__":
    N = max(1, int(input("Number of threads: ")))
    sums = [0 for _ in range(N)]
    lst = [i for i in range(1,10**6+1)]
    part_len = len(lst) // N
    start = time()
    threads = [
            Thread(target=lst_sum, args=(lst, i, i*part_len, (i+1)*part_len))
            for i in range(N)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Sum:", sum(sums))
    print("Time:", time() - start)
