n, k = map(int, input().split())
h = list(map(int, input().split()))

sol = float('inf')
t = sum(h[:k])
res = 0
i = 0
while i + k - 1 < n:
    # print(i+1, t, sum(h[i:i+k]), h[i:i+k])
    if sol > t:
        sol = t
        res = i
    if i + k == n: break 
    t = t - h[i] + h[i+k]
    i += 1
print(res + 1)