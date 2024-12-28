with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

l = []
d = {}
for j in range(len(a)):
    if a[j] in d.keys():
        l.append(f"{j+1} {d[a[j]] + 1}\n")
        del d[a[j]]
    else:
        d[a[j]] = j

# print(d, l)    
def print(s):
    with open('output.txt', 'w') as f:
        f.write(s)
if len(l) == n:
    print("".join(l))
else:
    print(str(-1))