n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

first = second = same = diff = 0
for i in l:
    a, b = i
    first += a
    second += b
    if a % 2 == b % 2:
        same += 1
    else:
        diff += 1

# print(first, second, same, diff)
if first % 2 == 0 and second % 2 == 0:
    print(0)
elif first % 2 == 1 and second % 2 == 1 and diff > 0:
    print(1)
else:
    print(-1)
    