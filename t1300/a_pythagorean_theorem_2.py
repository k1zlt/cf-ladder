import math
n = int(input())

s = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        c = math.sqrt(i**2 + j ** 2)
        if  1 <= i <= j <= c <= n and int(c) == c:
            # print(i, j, math.sqrt(i**2 + j ** 2))
            s += 1

print(s)