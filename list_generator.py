def triangles():
    n, L = 0, []
    while True:
        if n >0:
            tmp, o = [], 0
            for i, v in enumerate(L):
                if not i:
                    tmp.append(v)
                else:
                    o = L[i-1] + L[i]
                    tmp.append(o)
            L = tmp
        L.append(1)
        yield L
        n += 1


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
