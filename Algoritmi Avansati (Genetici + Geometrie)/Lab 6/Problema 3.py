from math import sqrt
import numpy as np

f = open("pb3.txt")  # fac citirea celor 4 puncte din fisier

A = list(map(float, f.readline().split()))  # citesc un rand si convertesc in float folosind map
print("A", A)  # [3.0, 1.0]

B = list(map(float, f.readline().split()))
print("B", B)  # [0.0, 3.0]

C = list(map(float, f.readline().split()))
print("C", C)  # [-3.0, 2.0]

D = list(map(float, f.readline().split()))
print("D", D)  # [-1.0, 0.0]

f.close()


def viraj(a, b, c):
    determinant = b[0] * c[1] + a[0] * b[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - a[0] * c[1]
    if determinant > 0:
        return 1  # viraj la stanga
    elif determinant < 0:
        return -1  # viraj la dreapta
    else:
        return 0  # coliniare


if viraj(A, B, C) != 1:  # nu e viraj si iau ACB
    tet = np.array([[A[0], A[1], A[0] ** 2 + A[1] ** 2, 1], [C[0], C[1], C[0] ** 2 + C[1] ** 2, 1], [B[0], B[1], B[0] ** 2 + B[1] ** 2, 1], [D[0], D[1], D[0] ** 2 + D[1] ** 2, 1]])
else:  # iau ABC
    tet = np.array([[A[0], A[1], A[0] ** 2 + A[1] ** 2, 1], [B[0], B[1], B[0] ** 2 + B[1] ** 2, 1], [C[0], C[1], C[0] ** 2 + C[1] ** 2, 1], [D[0], D[1], D[0] ** 2 + D[1] ** 2, 1]])
print(tet)
det = np.linalg.det(tet)  # calculez determinantul cu numpy

if det < 0:
    print("D este in <--AFARA--> cercului circumscris triunghiului ABC")  # D = (-6, 0)
elif det == 0:
    print("D este <--PE--> cercul circumscris triunghiului ABC")  # D = (0, 3)
else:
    print("D este <--IN--> cercul circumscris triunghiului ABC")  # D = (-1, 0)

# Incerc si a doua varianta, diferita fata de ideea din curs:

# Calculez pozitia relativa a lui D fata de cercul circumscris triung. ABC

# Vreau sa construiesc punctul de intersectie al mediatoarelor tri. ABC
# Apoi sa fac distanta de la acel punct la D si vad daca e in cerc, pe cerc sau in afara
# Voiam sa iau ecuatiile dreptelor (mediatoarelor) si sa caut punctul de intersectie pentru 2 dintre drepte.
# Am abandonat pentru ca trebuia sa rezolv cu un sistem de ecuatii.

# Am gasit pe wikipedia niste formule.

# Formulele: https://en.wikipedia.org/wiki/Circumscribed_circle#Circumcircle_equations

U = []  # intersectia mediatoarelor
X = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
print("X", X)

U.append(((A[0] ** 2 + A[1] ** 2) * (B[1] - C[1]) + (B[0] ** 2 + B[1] ** 2) * (C[1] - A[1]) + (C[0] ** 2 + C[1] ** 2) * (A[1] - B[1])) / X)
U.append(((A[0] ** 2 + A[1] ** 2) * (C[0] - B[0]) + (B[0] ** 2 + B[1] ** 2) * (A[0] - C[0]) + (C[0] ** 2 + C[1] ** 2) * (B[0] - A[0])) / X)
print("U", U)

# X 18.0
# U [-0.3888888888888889, -0.8333333333333334]

# Acum calculez distanta de la U la D, de la U la C (sau oricare alt punct dintre A,B,C)
# si daca prima distanta e mai mare ca a 2-a atunci
# este in afara, daca este egala atunci este pe cerc, altfel in cerc

UD = sqrt((D[0] - U[0]) ** 2 + (D[1] - U[1]) ** 2)
UC = sqrt((C[0] - U[0]) ** 2 + (C[1] - U[1]) ** 2)
print("UD", UD)
print("UC", UC)

if UD > UC:
    print("D este in <--AFARA--> cercului circumscris triunghiului ABC")  # D = (-6, 0)
elif UD == UC:
    print("D este <--PE--> cercul circumscris triunghiului ABC")  # D = (0, 3)
else:
    print("D este <--IN--> cercul circumscris triunghiului ABC")  # D = (-1, 0)
