lst = [-3, 5, 0, -8, 1, 10]

j = 0
i = 0
tmp = None



while j < len(lst):
    while i < len(lst):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
        i += 1
    j += 1
    i = j


print(lst)