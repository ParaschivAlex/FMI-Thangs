f = open('triunghi.txt', 'r')
v = []
for linie in f:
    lista = []
    linie = linie.split()
    for i in linie:
        lista.append(int(i))
    v.append(lista)

n = len(v)
smax = [[0 for i in range(n)] for j in range(n)]
smax[0][0] = v[0][0]

for i in range(n):
    for j in range(i+1):
        if j == 0:
            smax[i][j] = v[i][j] + smax[i-1][j]
        if i == j:
            smax[i][j] = v[i][j] + smax[i-1][j-1]
        else:
            smax[i][j] = v[i][j] + max(smax[i-1][j-1], smax[i-1][j])

print("Suma maxima este %s, pe drumul: " % max(smax[n-1]), end = '')

pozi = n-1
pozj = smax[n-1].index(max(smax[n-1]))
solutie = []

while pozi >= 0:
    solutie.append(v[pozi][pozj])
    if smax[pozi-1][pozj] >= smax[pozi-1][pozj-1]:
        pozi -= 1
    else:
        pozi -= 1
        pozj -= 1

for i in reversed(solutie):
    print(i, end = ' ')
f.close()