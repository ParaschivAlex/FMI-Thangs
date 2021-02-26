f = open('rucsac.txt', 'r')
n = int(f.readline())
v = []
for i in range(n):
    linie = f.readline().split()
    v.append((i + 1, int(linie[0]), int(linie[1]), int(linie[0]) / int(linie[1])))
G = int(f.readline())


def pivot(A):
    if len(A) <= 5:
        return sorted(A)[len(A) // 2]
    else:
        A.sort(key=lambda x: x[3])
        subliste = [A[i:i + 5] for i in range(0, len(A), 5)]
        mediane = [s1[len(s1) // 2] for s1 in subliste]
        return pivot(mediane)


solutie = []


def rezolvare_rucsac(v, G, f_pivot=pivot):
    global n, solutie
    pivot = f_pivot(v)[3]
    L = [x for x in v if x[3] < pivot]
    E = [x for x in v if x[3] == pivot]
    H = [x for x in v if x[3] > pivot]
    suma_H = sum(x[2] for x in H)
    if suma_H > G:
        return rezolvare_rucsac(H, G, f_pivot)
    if suma_H <= G:
        for elem in H:
            solutie.append([elem, 1])
            G -= elem[2]
        for elem in E:
            if elem[2] <= G:
                G -= elem[2]
                solutie.append([elem, 1])
            else:
                fractie = G / elem[2]
                solutie.append([elem, round(fractie, 3)])
                G = 0
            if G == 0:
                break
    if G > 0:
        rezolvare_rucsac(L, G, f_pivot)


rezolvare_rucsac(v, G)

print("Obiectele alese sunt:")
profit = 0
for elem in solutie:
    print("Obiectul %s - Cantitate %s" % (elem[0][0], elem[1]))
    profit += elem[0][1] * elem[1]
print("Profitul maxim este %s." % profit)
f.close()
