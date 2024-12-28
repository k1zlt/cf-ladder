n = int(input())
l = list(map(int, input().split()))

l.sort()
res = True
t = n // 3
for i in range(t):
    a, b, c = l[i], l[i + t], l[i + 2 * t]
    if c % b != 0 or b % a != 0 or b == c or a == b:
        res = False
        break

# print(l)
if res:
    for i in range(t):
        print(l[i], l[i + t], l[i + 2 * t])
else:
    print(-1)