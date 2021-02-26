f = open('subsircomun.txt', 'r')
c1 = f.readline().strip()
c2 = f.readline()
n = len(c1)
m = len(c2)
lmax = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if c1[i-1] == c2[j-1]:
            lmax[i][j] = 1 + lmax[i-1][j-1]
        else:
            lmax[i][j] = max(lmax[i][j-1], lmax[i-1][j])

print("Lungimea maxima a unui subsir comun este %s. Subsirul este: " % lmax[n][m], end = '')

i, j = n, m
solutie = []

while i > 0 and j > 0:
    if c1[i-1] == c2[j-1]:
        solutie.append(c1[i-1])
        i -= 1
        j -= 1
    else:
        if lmax[i][j-1] > lmax[i-1][j]:
            j -= 1
        else:
            i -= 1
for elem in reversed(solutie):
    print(elem, end = ' ')

f.close()