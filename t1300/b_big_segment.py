n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

l_min = float('inf')
r_max = float('-inf')

for i in l:
    l_min = min(l_min, i[0])
    r_max = max(r_max, i[1])

res = -2
for i in range(len(l)):
    if l[i][0] == l_min and l[i][1] == r_max:
        res = i
        break
    
print(res + 1)