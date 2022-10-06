t = "бааааа"
pi = [0]*len(t)
# Начальные условия
j = 0
i = 1
print(pi)
# Формирование массива pi
while i < len(t):
    if t[j] == t[i]:
        pi[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j-1]
print(pi)

# Поиск образа в строке
a = "ааааааааааааабаааааааааааа"
i = 0
j = 0
m = len(t)
n = len(a)

while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("Нашли!")
            break
    else:
        if j > 0:
            j = pi[j-1]
        else:
            i += 1
            if i == n:
                print("Нет такого")
                break
