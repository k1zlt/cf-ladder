a, b, c = map(int, input().split())

    
    
def calc(a, b, c):
    t = a * b * c
    if t == 1:
        return 1
    
    s = [0 for _ in range(a*b*c + 1)]
    for i in range(1, len(s)):
        for j in range(i, len(s), i):
            s[j] += 1
    k = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            for d in range(1, c+1):
                # print(i*j*d, s[i*j*d])
                k = (k + s[i*j*d]) % 1073741824
                
    return k

print(calc(a, b, c))