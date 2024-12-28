from collections import Counter

l = [
    [
        *[x for x in input()]
        ] for _ in range(4)
]
res = False
for i in range(3):
    for j in range(3):
        t = Counter([l[i][j], l[i][j+1], l[i+1][j], l[i+1][j+1]])
        if t["#"] < 2 or t["."] < 2:
            res = True
            break

print("YES" if res else "NO")