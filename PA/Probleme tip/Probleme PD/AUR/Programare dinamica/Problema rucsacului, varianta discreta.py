f = open('rucsac.txt', 'r')
n = int(f.readline())
v = []
for i in range(n):
    linie = f.readline().split()
    v.append((i+1, int(linie[0]), int(linie[1])))
G = int(f.readline())
cmax = [[0 for i in range(G+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, G+1):
        if v[i-1][1] > j:
            cmax[i][j] = cmax[i-1][j]
        else:
            cmax[i][j] = max(cmax[i-1][j], v[i-1][2] + cmax[i-1][j-v[i-1][1]])

print("Profitul maxim care poate fi obtinut este %s, introducand obiectele: " % cmax[n][G], end = '')

i, j = n, G
solutie = []

while i > 0:
    if cmax[i][G] != cmax[i-1][G]:
        solutie.append(v[i][0])
        j -= v[i][1]
        i -= 1
    else:
        i -= 1

for elem in reversed(solutie):
    print(elem, end = ' ')

f.close()