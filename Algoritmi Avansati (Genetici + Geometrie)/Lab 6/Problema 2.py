f = open("pb2.txt")
n = int(f.readline())

P = []
for i in range(n):
    x, y = f.readline().split()
    P.append((float(x), float(y)))  # citirea punctelor poligonului

print("n=", n, "      P=", P)

# pentru x-monotonie, de exemplu, vreau sa iau cel mai din stanga punct si sa parcurg punctele pentru ca sunt date in sens trigonometric
# si la fiecare punct verific monotonia lui x, iar dupa o parcurgere totala sa aiba o singura schimbare de monotonie
# pt y-monotonie ma duc din cel mai jos punct

# Prima data pentru x-monotonie

minim = P[0][0]
indexmin = -1
for i in range(len(P)):
    if P[i][0] < minim:
        minim = P[i][0]  # caut x-ul minim
        indexmin = i  # si retin si pozitia sa in poligon

monotonie, elem_precedent, okx = 1, P[indexmin][0], 0  # un boolean pt monotonie, o variabila unde retin elementul precedent si un boolean ok
for i in range(1, len(P)):  # parcurg toate celelalte puncte
    k = (i + indexmin) % len(P)  # formula pentru a lua in continuare punctele in sens trigonometric (adica pentru exemplul cu 6 puncte, aleg D si merg in continuare cu E,F,A,..)
    elem_curent = P[k][0]  # iau x-ul ca sa verific monotonia
    if elem_curent < elem_precedent:  # daca elemntul nou este mai mic decat cel precedent (daca se cerea monotonie strica puneam <=)
        monotonie = 0  # atunci am schimbat monotonia: ori nu e poligon x-monoton, ori am ajuns in cel mai din dreapta punct
    # am schimbat monotonia si ar trebui sa am doar elemente curente mai mici ca cele precedente
    if elem_curent > elem_precedent and monotonie == 0:  # daca intru pe if-ul asta atunci am schimbat monotonia si ar trebui sa am doar elemente curent mai mici ca cele precedente
        print("Poligonul NU este x-monoton!")  # evident daca nu e indeplinita conditia opresc si afisez ce trebuie
        okx = 1
        break
    elem_precedent = elem_curent  # elementul curent devinde cel precedent si parcurg in continuare
if okx == 0:
    print("Poligonul ESTE x-monoton!")

# la fel si pentru y-monotonie, aceleasi explicatii ca la x-monotonie doar ca parcurg din cel mai sudic punct pana la cel mai nordic
# si dupa verific invers proprietatea

minim = P[0][1]
indexmin = -1

for i in range(len(P)):
    if P[i][1] < minim:
        minim = P[i][1]  # caut y-ul minim
        indexmin = i  # si retin si pozitia sa in poligon

monotonie, elem_precedent, oky = 1, P[indexmin][1], 0
for i in range(1, len(P)):  # parcurg toate celelalte puncte
    k = (i + indexmin) % len(P)
    elem_curent = P[k][1]
    if elem_curent < elem_precedent:  # pentru ca nu se cere strict monotonie, nu caut cu <=
        monotonie = 0  # am schimbat monotonia, ori nu e poligon y-monoton, ori am ajuns in cel mai de sus punct
    if elem_curent > elem_precedent and monotonie == 0:
        print("Poligonul NU este y-monoton!")
        oky = 1
        break
    elem_precedent = elem_curent
if oky == 0:
    print("Poligonul ESTE y-monoton!")

# pentru n = 6 si punctele aferente :
# n= 6      P= [(4.0, 5.0), (5.0, 7.0), (5.0, 9.0), (2.0, 5.0), (4.0, 2.0), (6.0, 3.0)]
# Poligonul NU este x-monoton!
# Poligonul ESTE y-monoton!

# pentru n = 8 si punctele aferente
# n= 8       P= [(8.0, 7.0), (7.0, 5.0), (4.0, 5.0), (3.0, 9.0), (0.0, 1.0), (5.0, 2.0), (3.0, 3.0), (10.0, 3.0)]
# Poligonul NU este x-monoton!
# Poligonul NU este y-monoton!
