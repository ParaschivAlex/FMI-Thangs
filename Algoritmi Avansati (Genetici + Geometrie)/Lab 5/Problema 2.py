# Citirea din fisier

f = open("pb2.txt")

n = int(f.readline())
puncte = []

for i in range(n):
    punct = f.readline().split()
    # print(punct[0], punct[1])
    puncte.append((float(punct[0]), float(punct[1])))
f.close()

print("Punctele dupa citire:", puncte)


def viraj_dreapta_sau_colin(a, b, c):
    return (b[0] * c[1] + a[0] * b[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - a[0] * c[1]) <= 0  # functia de la problema 1, as fi putut sa fac operatii si sa calculez determinantul altfel


# determinant = xq * yr + xp * yq + xr * yp - xq * yp - xr * yq - xp * yr

def compute_hull():
    hull = [(puncte[0][0], puncte[0][1]), (puncte[1][0], puncte[1][1])]  # adaug primele 2 puncte in stiva

    i = 2
    while i < len(puncte):  # parcurg toate punctele
        hull.append((puncte[i][0], puncte[i][1]))  # incep sa adaug cate un punct
        print(hull, viraj_dreapta_sau_colin(hull[-3], hull[-2], hull[-1]))  # afisare pt debug
        while len(hull) >= 3 and viraj_dreapta_sau_colin(hull[-3], hull[-2], hull[-1]):  # daca am viraj la dreapta sau puncte coliniare scot penultimul nod(punct) cat timp am
            # cel putin 2 noduri in stiva si cat timp am viraj la dreapta
            hull.pop(-2)
        i += 1

    return hull


puncte.sort()  # sortez crescator ca sa incep cu cel mai din stanga pt ca se afla sigur pe frontiera
print("Punctele dupa prima sortare", puncte)
stanga_start = compute_hull()  # rezolv pt partea inferioara

print("Stanga ", stanga_start)
puncte.reverse()  # apoi incep invers si rezolv pt partea superioara
dreapta_start = compute_hull()
print("Dreapta ", dreapta_start)
solutie = stanga_start + dreapta_start[1:]  # unesc rezultatele si afisez

print("Lungimea drumului:", len(solutie) - 1)
print("Traseul:", solutie)  # da corect
