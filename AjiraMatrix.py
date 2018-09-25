import numpy as np


def cal(a, i, t):
    t = -1
    for j in range(i + 1, len(a[i])):
        if (a[i][j] == 'R'):
            t = i
    return t


a, c, temp, t = [], 0, [], -1
x = list(input().split())
# a=list(list(input().split()))
a.append(x)
# print(len(x))
for i in range(len(x) - 1):
    x = list(input().split())
    a.append(x)
for l in range(len(a)):
    for i in range(len(a)):
        t = -1
        f = cal(a, i, t)
        if (f != -1):
            for k in range(len(a)):
                if (f != k):
                    for k in range(len(a)):
                        if (f != k):
                            temp = a[f]
                            a[f] = a[k]
                            a[k] = temp
                            f = cal(a, i, t)
                            if (k == -1):
                                break

print(np.asarray(a))
print(c)
