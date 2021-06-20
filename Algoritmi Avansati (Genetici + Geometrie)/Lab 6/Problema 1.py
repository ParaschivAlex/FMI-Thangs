# Datele din fisier sunt aceleasi ca in laborator

# import numpy as np
from math import sqrt

# Citesc datele din fisier

f = open("pb1.txt")

n = int(f.readline())
# print("n", n)

P = []  # aici pun punctele poligonului
Q = []  # aici pun punctul pentru care vreau sa ii aflu pozitia relativa fata de P

for i in range(n):
    x, y = f.readline().split()
    P.append((float(x), float(y)))  # citirea punctelor poligonului
x, y = f.readline().split()
Q.append(float(x))
Q.append(float(y))  # citirea punctului pe care il caut

max_x = max(P)  # caut si cel mai mare x ca sa fiu sigur ca iau M in afara poligonului
print("Maximul X:", max_x)

f.close()
print("P", P)
print("Q", Q)


def viraj(a, b, c):  # functie ca in lab 5 pb 2 in care verific virajul
    determinant = b[0] * c[1] + a[0] * b[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - a[0] * c[1]
    if determinant > 0:
        return 1  # viraj la stanga
    elif determinant < 0:
        return -1   # viraj la dreapta
    else:
        return 0  # coliniare


def distanta(a, b):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


M = [max_x[0] + 10, Q[1]]  # iau un punct M in functie de valorile calculate anterior (max_x + 10, 10 luat random si y-ul lui Q)
print("M", M)

nr_intersectii = 0  # si vad de cate ori intersecteaza dreapta QM poligonul, daca e par se afla in exteriorul poligonului, daca e impar e in interior
# pentru cazul in care e pe o latura a poligonului verific daca prin functia viraj daca sunt coliniare punctele (+ distanta ca sa fiu sigur ca e pe latura)
# de asemenea, tratez si cazurile speciale relatate in laborator prin supremum si infimum.

ok = 0  # ok pt oprit forul urmator daca gasesc puncte coliniare (si pe aceeasi dreapta)

for i in range(0, n - 1, 1):
    if viraj(P[i], P[i + 1], Q) == 0 and distanta(P[i], Q) + distanta(P[i + 1], Q) == distanta(P[i], P[i + 1]):  # verific daca Q e pe dreapta
        print("Punctul este PE UNA DINTRE laturile poligonului.")  # aici se termina
        ok = 1
        break
    # print(i)
    # print(viraj(P[i], P[i + 1], Q) == 0)
    # print(distanta(P[i], Q), distanta(P[i + 1], Q))
    # print("------------------------")
# print("OK", ok)
if viraj(P[-1], P[0], Q) == 0 and distanta(P[-1], Q) + distanta(P[0], Q) == distanta(P[0], P[-1]):  # verific si ultimul punctul cu primul
    print("Punctul este PE UNA DINTRE laturile poligonului.")  # aici se termina
    ok = 1

verif = [0 for _ in range(n)]  # fac o lista verif initializata cu 0. Modific in 1 atunci cand gasesc un punct care e pe dreapta QM

if ok == 0:  # daca nu e pe nicio dreapta atunci continui
    for i in range(0, n - 1, 1):
        if P[i][1] == Q[1] and P[i][0] > Q[0]:  # verific daca dreapta QM trece printr-un varf. Fac asta prin ecuatia dreptei care da mereu y = Q[1] pentru ca QM este paralela la Ox
            print("QM trece prin punctul", P[i])
            verif[i] = 1
            verif[i - 1] = 1
            verif[i + 1] = 1
            if (P[i - 1][1] > P[i][1] and P[i + 1][1] <= P[i][1]) or (P[i - 1][1] <= P[i][1] and P[i + 1][1] > P[i][1]):  # acum verific daca e supremum pt un punct si infimum pentru celalalt (alea de langa) ca sa pot aduna 1 la intersectii. Altfel adunam 2 sau 0, dar nu adun nimic ca e acelasi lucru
                nr_intersectii += 1

if P[-1][1] == Q[1] and P[-1][0] > Q[0]:  # acelasi lucru pt ultimul punct si primul
    print("QM trece prin punctul", P[-1])
    verif[-1] = 1
    verif[-2] = 1
    verif[0] = 1
    if (P[-2][1] > P[-1][1] and P[0][1] <= P[-1][1]) or (P[-2][1] <= P[-1][1] and P[0][1] > P[-1][1]):
        nr_intersectii += 1

if ok == 0:
    for i in range(0, n - 1, 1):
        if verif[i] == 0:
            if viraj(P[i], P[i + 1], Q) != viraj(P[i], P[i + 1], M) and viraj(Q, M, P[i]) != viraj(Q, M, P[i + 1]):  # verific cu functia viraj daca se intersecteaza segmentele (daca nu a trecut printr-un punct la pasul anterior)
                nr_intersectii += 1
                print("QM intersecteaza dreapta", P[i], P[i + 1])  # afisez si ce segmente intersecteaza

if verif[-1] == 0:
    if viraj(P[-1], P[0], Q) != viraj(P[-1], P[0], M) and viraj(Q, M, P[-1]) != viraj(Q, M, P[0]):  # acelasi lucru pt ultimul punct si primul
        nr_intersectii += 1
        print("QM intersecteaza dreapta", P[-1], P[0])

if ok == 0:
    print("Numarul de intersectii:", nr_intersectii)
if nr_intersectii % 2 != 0 and ok == 0:  # daca intersecteaza de un nr impar de ori si nu am gasit sa fie Q pe o dreapta, atunci e in INTERIOR
    print("Punctul este in INTERIORUL poligonului.")
elif nr_intersectii % 2 == 0 and ok == 0:  # altfel in EXTERIOR
    print("Punctul este in EXTERIORUL poligonului.")
