n = int(input())
if sum(list(map(int, input().split()))) % n == 0:
    print(n)
else:
    print(n - 1)