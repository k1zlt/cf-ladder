from collections import Counter

n = int(input())
w = Counter(input().split())

w1 = w['200'] // 2
w2 = w['200'] - w1

sol = True

if w1 == w2:
    if w['100'] % 2 != 0:
        sol = False
else:
    if w['100'] < 2:
        sol = False
    elif w['100'] % 2 != 0:
        sol = False
    

print("YES" if sol else "NO")