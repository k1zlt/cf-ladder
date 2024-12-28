d = {
    25: 0,
    50: 0,
    100: 0
}
n = int(input())
l = list(map(int, input().split()))
res = True
for i in l:
    # print(i, d)
    if i == 25:
        d[25] += 1
    elif i == 50:
        if d[25] >= 1:
            d[25] -= 1
            d[50] += 1
        else:
            res = False
            break
    else:
        if d[50] >= 1 and d[25] >= 1:
            d[50] -= 1
            d[25] -= 1
        elif d[25] >= 3:
            d[25] -= 3
        else:
            res = False
            break

print("YES" if res else "NO")