# Citirea din fisier
from math import sqrt

f = open("pb4.txt")

n = int(f.readline())
puncte = []

for i in range(n):
    punct = f.readline().split()
    # print(punct[0], punct[1])
    puncte.append((float(punct[0]), float(punct[1])))

f.close()
print(n, puncte)


# primul pas e la fel ca la pb 2

def viraj_dreapta_sau_colin(a, b, c):
    return (b[0] * c[1] + a[0] * b[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - a[0] * c[1]) <= 0  # functia de la problema 1, as fi putut sa fac operatii si sa calculez determinantul altfel


# determinant = xq * yr + xp * yq + xr * yp - xq * yp - xr * yq - xp * yr

def compute_hull():
    hull = [(puncte[0][0], puncte[0][1]), (puncte[1][0], puncte[1][1])]  # adaug primele 2 puncte in stiva

    i = 2
    while i < len(puncte):  # parcurg toate punctele
        hull.append((puncte[i][0], puncte[i][1]))  # incep sa adaug cate un punct
        # print(hull, viraj_dreapta_sau_colin(hull[-3], hull[-2], hull[-1])) #afisare pt debug
        while len(hull) >= 3 and viraj_dreapta_sau_colin(hull[-3], hull[-2], hull[-1]):  # daca am viraj la dreapta sau puncte coliniare scot penultimul nod(punct) cat timp am
            # cel putin 2 noduri in stiva si cat timp am viraj la dreapta
            hull.pop(-2)
        i += 1

    return hull


puncte.sort()  # sortez crescator ca sa incep cu cel mai din stanga pt ca se afla sigur pe frontiera
# print("Punctele dupa prima sortare", puncte)
stanga_start = compute_hull()  # rezolv pt partea inferioara

# print("Stanga ", stanga_start)
puncte.reverse()  # apoi incep invers si rezolv pt partea superioara
dreapta_start = compute_hull()
# print("Dreapta ", dreapta_start)
solutie = stanga_start + dreapta_start[1:]  # unesc rezultatele si afisez

print("Lungimea drumului:", len(solutie))
print("Traseul:", solutie)  # da corect

puncte_ramase = set(puncte) - set(solutie)  # fac set ca sa fac diferenta dintre toate si cele folosite
puncte_ramase = list(puncte_ramase)  # transform inapoi in lista de tupluri desi nu are vreo importanta, cred


def cijr_formula_distante(a, b, c):  # a,b,c este in ordinea i,j,r
    return sqrt(((a[0] - c[0]) ** 2) + (a[1] - c[1]) ** 2) + sqrt(((b[0] - c[0]) ** 2) + (b[1] - c[1]) ** 2) - sqrt(((a[0] - b[0]) ** 2) + (a[1] - b[1]) ** 2)


print("-------------------CHECKPOINT------------------")

ok = 1  # devine 0 cand nu mai avem elemente de adaugat
while ok:
    print("Punctele ramase de adaugat:", puncte_ramase)
    pereche_ijr = []
    valori = []
    for k in range(len(puncte_ramase)):  # pentru fiecare nod r caut cele 2 puncte pt care formula e minima
        i, j = (0, 0), (0, 0)
        val = 0
        Cijr_minimal = 99999
        # Aici e asa daca caut (I,J) oricare 2 puncte. Am comentat varianta si am implementat una mai buna in care iau (I,J) puncte consecutive.
        # for m in range(len(solutie)-1):
        #     for n in range(m+1, len(solutie)):
        #         val = cijr_formula_distante(solutie[m], solutie[n], puncte_ramase[k])
        #         if Cijr_minimal > val:
        #             Cijr_minimal = val
        #             i = solutie[m]
        #             j = solutie[n]

        for m in range(len(solutie) - 1):
            val = cijr_formula_distante(solutie[m], solutie[m + 1], puncte_ramase[k])
            if Cijr_minimal > val:
                Cijr_minimal = val
                i = solutie[m]
                j = solutie[m + 1]
        pereche_ijr.append((i, j, puncte_ramase[k]))
        valori.append(val)

    # pasul 3, pentru fiecare pereche de la pasul anterior caut o singura pereche care are valoarea minima

    poz_val_min = valori.index(min(valori))
    poz_pt_add = 0
    print("Perechile (i,j,r), valorile calculate si pozitia minimului:", pereche_ijr, valori, poz_val_min)
    if pereche_ijr[poz_val_min][0] == solutie[0]:  # aici aparea o problema daca era legat pe primul nod ca am facut afisarea mai ciudata si se lega de parcurgerea in sens trigonometric
        # desi trebuia invers. Asa ca testez sa vad care e celalalt punct ca sa stiu unde il bag
        if pereche_ijr[poz_val_min][1] == solutie[-2]:
            poz_pt_add = solutie.index(pereche_ijr[poz_val_min][1]) + 1
    else:
        poz_pt_add = solutie.index(pereche_ijr[poz_val_min][0]) + 1  # caut pozitia undex sa adaug nodul nou
    print("Pozitia unde trebuie adaugat punctul nou = ", poz_pt_add)
    solutie.insert(poz_pt_add, pereche_ijr[poz_val_min][2])
    print("Solutia pentru pasul curent:", solutie)
    puncte_ramase.remove(pereche_ijr[poz_val_min][2])

    if len(puncte_ramase) == 0:
        ok = 0

print("======================================================================================================================================")
print("Solutia finala este:", solutie)
lungime_drum = 0
for i in range(len(solutie) - 1):
    lungime_drum += sqrt(((solutie[i][0] - solutie[i + 1][0]) ** 2) + (solutie[i][1] - solutie[i + 1][1]) ** 2)
print("Lungimea calculata este:", lungime_drum)
