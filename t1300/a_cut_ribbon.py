n, a, b, c = map(int, input().split())

l = [-1 for _ in range(n+1)]

l[0] = 0

for i in range(n):
    if l[i] == -1: continue
    
    if i + a < len(l):
        l[i+a] = max(l[i+a], l[i] + 1)
    if i + b < len(l) and a != b:
        l[i+b] = max(l[i+b], l[i] + 1)
    if i + c < len(l) and a != c and b != c:
        l[i+c] = max(l[i+c], l[i] + 1)
    # print(l)
        
print(l[-1])