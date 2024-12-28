n, k = map(int,  input().split())
l = [tuple(map(int, input().split())) for _ in range(n)]

l.sort(key=lambda x: x[1])
l.sort(key=lambda x: -x[0])

t = l[k - 1]
res = 0
for i in range(len(l)):
    if l[i] == t: res += 1

# print(n, k, l)
print(res)