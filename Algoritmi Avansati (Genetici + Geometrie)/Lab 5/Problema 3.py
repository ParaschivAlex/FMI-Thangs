# Citirea din fisier
import copy
from math import sqrt

f = open("pb3.txt")

n = int(f.readline())
puncte = []

for i in range(n):
    punct = f.readline().split()
    # print(punct[0], punct[1])
    puncte.append((float(punct[0]), float(punct[1])))

x = tuple(map(float, f.readline().split()))
f.close()
print(n, puncte, x)


def viraj(a, b, c):
    if (b[0] * c[1] + a[0] * b[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - a[0] * c[1]) > 0:
        return 1
    elif (b[0] * c[1] + a[0] * b[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - a[0] * c[1]) < 0:
        return -1
    else:
        return 0


def caut_bin_punct():
    lg = copy.copy(n)
    poligon = copy.deepcopy(puncte)
    if x in poligon:
        return 0  # E chiar un punct din cele date deci e pe frontiera
    while lg > 3:  # ma opresc cand ajung la ultimul triungi
        mid = lg // 2
        if viraj(poligon[0], poligon[mid], x) > 0:  # e viraj la stanga si cautam in partea stanga
            for i in range(mid - 1, 0, -1):
                poligon.pop(i)

        elif viraj(poligon[0], poligon[mid], x) < 0:  # in cazul asta la dreapta
            for i in range(len(poligon) - 1, mid, -1):
                poligon.pop(i)

        else:  # coliniare...
            # daca distanta AX + XB = AB atunci e in poligon, altfel e in afara. Cazul X = un punct din poligon este la inceput
            ax = sqrt(((x[0] - poligon[0][0]) ** 2) + (x[1] - poligon[0][1]) ** 2)
            bx = sqrt(((poligon[mid][0] - x[0]) ** 2) + (poligon[mid][1] - x[1]) ** 2)
            ab = sqrt(((poligon[mid][0] - poligon[0][0]) ** 2) + (poligon[mid][1] - poligon[0][1]) ** 2)

            if ax + bx == ab:
                return 1
            else:
                return -1
        print(poligon, '\n', mid, "Lungimea precedenta", lg)
        lg = len(poligon)
        print("Lungimea actuala", lg)

    print("Checkpoint :)")
    print(poligon, '\n')
    # cand am ajuns la triunghiul final verific daca e in el, in afara sau pe vreo latura
    # prima data verific daca e pe latura:
    pm = sqrt(((poligon[1][0] - poligon[2][0]) ** 2) + (poligon[2][1] - poligon[1][1]) ** 2)
    px = sqrt(((poligon[1][0] - x[0]) ** 2) + (poligon[1][1] - x[1]) ** 2)
    xm = sqrt(((poligon[2][0] - x[0]) ** 2) + (poligon[2][1] - x[1]) ** 2)
    if px + xm == pm and viraj(poligon[1], poligon[2], x) == 0:
        return 0
    if viraj(poligon[1], poligon[2], x) > 0 and viraj(poligon[2], poligon[0], x) > 0 and viraj(poligon[0], poligon[1], x) > 0:  # atunci e in cerc, > si nu are cum sa fie = ca am verificat mai sus
        return 1
    else:
        return -1


print(caut_bin_punct())
