

a = list(range(1, 10000, 1))
n = len(a) - 1
for k in range(1, n):
    for i in range(1, n):
        a[i] = (a[i-1] + a[i] + a[i+1]) / 3.0