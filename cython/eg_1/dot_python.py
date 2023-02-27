# dot_python.py
import numpy as np

def naive_dot(a, b):
    if a.shape[1] != b.shape[0]:
        raise ValueError('shape not matched')
    n, p, m = a.shape[0], a.shape[1], b.shape[1]
    c = np.zeros((n, m), dtype=np.float32)
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(p):
                s += a[i, k] * b[k, j]
            c[i, j] = s
    return c

if __name__ == "__main__":
    a = np.random.rand(5,6)
    b = np.random.rand(6,7)
    print(a)
    print(b)
    for i in range(10000):
        c = naive_dot(a, b)
    print(c)