y, k, n = map(int, input().split())

x = max(1, k - y % k)
t = True
while x + y <= n:
    print(x, end = " ")
    x += k
    t = False

if y >= n or t:
    print(-1)