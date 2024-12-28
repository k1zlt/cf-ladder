a = input()
b = input()

if len(a) != len(b):
    print("NO")
else:
    l = []
    for i in range(len(a)):
        if a[i] != b[i]:
            l.append(i)
    if len(l) == 2:
        if a[l[0]] == b[l[1]] and a[l[1]] == b[l[0]]:
            print("YES")
        else:
            print("NO")
    else:
        print('NO')