lst = [-3, 5, 0, -8, 1, 10, -10, 12]


j = 1

while j < len(lst)-2:
    for k in range(j + 1, -1, -1):
        if lst[k+1] < lst[k]:
            lst[k], lst[k+1] = lst[k+1], lst[k]
    j += 1

print(lst)


