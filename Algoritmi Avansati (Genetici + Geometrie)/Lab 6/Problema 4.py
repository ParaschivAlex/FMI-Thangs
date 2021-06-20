from math import sqrt
import numpy as np

f = open("pb4.txt")  # fac citirea exact ca la problema 3

A = list(map(float, f.readline().split()))
print("A", A)

B = list(map(float, f.readline().split()))
print("B", B)

C = list(map(float, f.readline().split()))
print("C", C)

D = list(map(float, f.readline().split()))
print("D", D)

f.close()


# ideea rezolvarii este aproape ca la problema 3, pentru diagonala AC vad cum este D fata de cercul circumscris ABC
# iar pentru BD vad cum e C fata de cercul circumscris ABD
# apoi daca acel punct este in interior atunci este muchie ilegala, altfel legala.

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
det = np.linalg.det(tet)

if viraj(A, B, D) != 1:  # nu e viraj si iau ADB
    tet2 = np.array([[A[0], A[1], A[0] ** 2 + A[1] ** 2, 1], [D[0], D[1], D[0] ** 2 + D[1] ** 2, 1], [B[0], B[1], B[0] ** 2 + B[1] ** 2, 1], [C[0], C[1], C[0] ** 2 + C[1] ** 2, 1]])
else:  # iau ABD
    tet2 = np.array([[A[0], A[1], A[0] ** 2 + A[1] ** 2, 1], [B[0], B[1], B[0] ** 2 + B[1] ** 2, 1], [D[0], D[1], D[0] ** 2 + D[1] ** 2, 1], [C[0], C[1], C[0] ** 2 + C[1] ** 2, 1]])
print(tet)
det2 = np.linalg.det(tet2)

if det > 0:
    print("Muchia AC este ilegala")
else:
    print("Muchia AC este legala")

if det2 > 0:
    print("Muchia BD este ilegala")
else:
    print("Muchia BD este legala")

# Inca o solutie bazata pe formulele de calcul din a doua solutie de la problema 3

print("Solutia 2:")

U = []  # intersectia mediatoarelor pentru ABC
W = []  # ----------||||----------- pentru ABD
X = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
Y = 2 * (A[0] * (B[1] - D[1]) + B[0] * (D[1] - A[1]) + D[0] * (A[1] - B[1]))
# print("X", X)
# print("Y", Y)

U.append(((A[0] ** 2 + A[1] ** 2) * (B[1] - C[1]) + (B[0] ** 2 + B[1] ** 2) * (C[1] - A[1]) + (C[0] ** 2 + C[1] ** 2) * (A[1] - B[1])) / X)
U.append(((A[0] ** 2 + A[1] ** 2) * (C[0] - B[0]) + (B[0] ** 2 + B[1] ** 2) * (A[0] - C[0]) + (C[0] ** 2 + C[1] ** 2) * (B[0] - A[0])) / X)

W.append(((A[0] ** 2 + A[1] ** 2) * (B[1] - D[1]) + (B[0] ** 2 + B[1] ** 2) * (D[1] - A[1]) + (D[0] ** 2 + D[1] ** 2) * (A[1] - B[1])) / X)
W.append(((A[0] ** 2 + A[1] ** 2) * (D[0] - B[0]) + (B[0] ** 2 + B[1] ** 2) * (A[0] - D[0]) + (D[0] ** 2 + D[1] ** 2) * (B[0] - A[0])) / X)
# print("U", U)
# print("W", W)

UD = sqrt((D[0] - U[0]) ** 2 + (D[1] - U[1]) ** 2)
UC = sqrt((C[0] - U[0]) ** 2 + (C[1] - U[1]) ** 2)

WC = sqrt((C[0] - W[0]) ** 2 + (C[1] - W[1]) ** 2)
WD = sqrt((D[0] - W[0]) ** 2 + (D[1] - W[1]) ** 2)

# print("UD", UD)
# print("UC", UC)

# Am aplicat aceleasi formule ca la problema 3

if UD < UC:
    print("Muchia AC este ilegala")
else:
    print("Muchia AC este legala")

if WC < WD:
    print("Muchia BD este ilegala")
else:
    print("Muchia BD este legala")
