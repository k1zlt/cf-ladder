from collections import Counter

s1 = dict(Counter(input()))
s2 = dict(Counter(input()))
res = True
for key, value in s2.items():
    if key == " " or key == "\n": continue
    if key not in s1.keys() or s1[key] < value:
        res = False
        break

print("YES" if res else "NO")