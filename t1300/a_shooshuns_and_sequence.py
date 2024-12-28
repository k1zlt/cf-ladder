n, k = map(int, input().split())
a = list(map(int, input().split()))

def count_n(a, t):
    w = 0
    nw = 0
    for i in a:
        if i == t:
            w += 1
        else:
            nw += 1
    return w, nw

def calc():
    t = a[k-1]
    w, nw = count_n(a, t)
    c = 0
    for i in range(k):
        if nw == 0:
            return c
        c += 1
        if a[i] == t:
            w -= 1
        else:
            nw -= 1
    return -1

print(calc())