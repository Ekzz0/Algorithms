a = [1, 4, 5, 10]
b = [3, 4, 6, 10, 11, 12]
def merge_list(a,b):
    res = []
    i = 0
    j = 0
    N = len(a)
    M = len(b)
    while i < N and j < M:
        if a[i] >= b[j]:
            res.append(b[j])
            j += 1
        else:
            res.append(a[i])
            i += 1
    res += a[i:] + b[j:]
    return res