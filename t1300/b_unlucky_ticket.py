n = int(input())
a = input()

a1 = sorted([int(_) for _ in a[:n]])
a2 = sorted([int(_) for _ in a[n:]])

def check(a1, a2):
    for i in range(len(a1)):
        if a1[i] <= a2[i]: return False
        
    return True

print("YES" if (check(a1, a2) if a1[0] > a2[0] else check(a2, a1)) else "NO")