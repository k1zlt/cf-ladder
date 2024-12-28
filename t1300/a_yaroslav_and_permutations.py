from collections import Counter
import math

n = int(input())
a = list(map(int, input().split()))


print("YES" if max(Counter(a).values()) <= math.ceil(n / 2) else 'NO')