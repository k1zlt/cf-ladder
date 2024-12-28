from itertools import permutations

def calc(perm, l):
    s = 0
    for i in range(5):
        for j in range(i, 5, 2):
            if j+1 > 4: continue
            s += l[perm[j]][perm[j+1]] + l[perm[j+1]][perm[j]]
    return s

l = [list(map(int, input().split())) for i in range(5)]

m = 0
for i in list(permutations(range(5))):
    m = max(m, calc(i, l))
    
print(m)
# print(calc([1, 2, 0, 4, 3], l))