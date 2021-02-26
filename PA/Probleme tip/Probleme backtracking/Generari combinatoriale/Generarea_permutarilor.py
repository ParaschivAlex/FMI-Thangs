def bkt(k):
    global n, sol

    for v in range(1, n+1):
        sol[k] = v
        if v not in sol[:k]:
            if k == n-1:
                print(sol)
            else:
                bkt(k+1)

n = 4
sol = [0]*n
bkt(0)


