f = open('subsir.txt', 'r')
v = [int(i) for i in f.readline().split()]
n = len(v)
lmax = [1 for i in range(n)]
succ = [-1 for i in range(n)]
lmax[n-1] = 0
def gasesteSuccesor(i):
    global v, lmax, n
    nrMinSuccesor = 1
    Succesor = -1
    for j in range(i+1, n):
        if v[i] <= v[j]:
            if lmax[j] >= nrMinSuccesor:
                Succesor = j
                nrMinSuccesor = lmax[j] + 1
    return nrMinSuccesor, Succesor

for i in range(n-1, -1, -1):
    lmax[i], succ[i] = gasesteSuccesor(i)

print("Lungimea maxima a unui subsir strict crescator este %s. Sirul este: " % max(lmax), end = '')
k = lmax.index(max(lmax))
while k < n and k != -1:
    print(v[k], end = ' ')
    k = succ[k]

f.close()