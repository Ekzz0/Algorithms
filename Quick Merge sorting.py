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

def merged_sorting(a):
    N1 = len(a)//2
    left = a[:N1]
    right = a[N1:]

    if len(left) > 1:
        left = merged_sorting(left)

    if len(right) > 1:
        right = merged_sorting(right)

    return merge_list(left, right)




a = [1, -6, -5, 2, -10]

print(merged_sorting(a))