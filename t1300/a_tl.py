n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def min_max(l):
    min_value = float("inf")
    max_value = float("-inf")
    for i in l:
        min_value, max_value = min(i, min_value), max(i, max_value)
    return min_value, max_value

a_min, a_max = min_max(a)
b_min, b_max = min_max(b)

if max(a_max, a_min * 2) < b_min:
    print(max(a_max, a_min * 2))
else:
    print(-1)