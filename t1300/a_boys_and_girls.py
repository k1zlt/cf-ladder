with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    
def print(s):
    with open('output.txt', 'w') as f:
        f.write(s)

if n == m:
    print("BG" * n)
if n > m:
    print("BG" * m + ("B" * (n - m)))
if n < m:
    print("GB" * n + ("G" * (m - n)))