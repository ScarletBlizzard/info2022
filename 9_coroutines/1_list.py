lst = [1,2,3,4,5]
for i in lst:
    lst.append(i) # changing list
    if i == 5:
        break
print(lst)
