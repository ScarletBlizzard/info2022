# Selection sort
lst = list(map(int, input().split(',')))
for i in range(len(lst)-1):
    min_i = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[min_i]:
            min_i = j
    lst[i], lst[min_i] = lst[min_i], lst[i]
print(lst)
