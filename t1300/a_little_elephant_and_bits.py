n = [_ for _ in input()]
t = False
for i, v in enumerate(n):
    if v == "0":
        del n[i]
        t = True
        # print(i, v)
        break

if t:
    print("".join(n))
else:
    print("".join(n[1:]))