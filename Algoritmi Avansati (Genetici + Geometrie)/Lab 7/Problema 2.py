# Paraschiv Alexandru-Andrei
# Grupa 243

f = open("pb2.txt")

Q = tuple(map(float, f.readline().split()))  # citesc Q din fisier
print(Q)

n = int(f.readline())
print(n)

inf_x, sup_x, inf_y, sup_y, inf_x2, sup_x2, inf_y2, sup_y2 = -99999, 99999, -99999, 99999, -99999, 99999, -99999, 99999
x_neg, x_poz, y_neg, y_poz = 0, 0, 0, 0
drepte = []
marginita = 0
for i in range(n):  # la fel ca la problema 1
    a, b, c = f.readline().split()
    drepte.append([float(a), float(b), float(c)])
    if drepte[i][0] == 0:  # daca x == 0. In continuare am renuntat la x_neg si celelalte variabile fata de problema 1
        c_nou_y = drepte[i][2] / drepte[i][1] * (-1)  # calculez ca la problema 1
        if drepte[i][1] <= Q[1]:  # daca y-ul este mai mic sau egal ca si y-ul lui Q ca sa gasesc Q in dreptunghi
            if c_nou_y > inf_y:  # daca valoarea calculata anterior > inf_y atunci inf_y ia valoarea si pun si urmatoarea valoare cea mai mica in inf_y2
                inf_y = c_nou_y
                inf_y2 = inf_y
                y_neg = 1
            elif c_nou_y > inf_y2:  # daca nu, verific daca e mai mare ca si inf_y2 si pun acolo
                inf_y2 = c_nou_y
        else:  # daca y-ul este mai mare ca si y-ul lui Q
            if c_nou_y < sup_y:  # la fel dar pentru sup_y
                sup_y = c_nou_y
                sup_y2 = sup_y
                y_poz = 1
            elif c_nou_y < sup_y2:
                sup_y = c_nou_y
    else:  # exact la fel dar pentru y == 0
        c_nou_x = drepte[i][2] / drepte[i][0] * (-1)
        if drepte[i][0] <= Q[0]:
            if c_nou_x > inf_x:
                inf_x = c_nou_x
                inf_x2 = inf_x
                x_neg = 1
            elif c_nou_x > inf_x2:
                inf_x2 = c_nou_x
        else:
            if c_nou_x < sup_x:
                sup_x = c_nou_x
                sup_x2 = sup_x
                x_poz = 1
            elif c_nou_x < sup_x2:
                sup_x2 = c_nou_x

print("Valorile -->", drepte)
print("Inf_x, Sup_x, Inf_y, Sup_y  --->   ", inf_x, sup_x, inf_y, sup_y)
print("Inf_x2, Sup_x2, Inf_y2, Sup_y2  --->   ", inf_x2, sup_x2, inf_y2, sup_y2)

f.close()

# acum verific ca in problema 1 daca s-au schimbat valorile pentru a avea marginit = 1
if x_neg != 0 and x_poz != 0 and y_neg != 0 and y_poz != 0:
    marginita = 1

if marginita:
    arie = (sup_x - inf_x) * (sup_y - inf_y)  # calculez aria
    if arie:  # daca este strict pozitiva
        print("EXISTA un dreptunghi cu proprietatea ceruta. Valoarea nimina a ariilor dreptunghiurilor cu proprietatea ceruta este", arie)
    else:  # altfel calculez toate ariile care mai pot rezulta si iau minimul

        arie_minima, arie_noua = -1, []
        arie_noua.append((sup_x2 - sup_x) * (sup_y2 - sup_y))
        arie_noua.append((inf_x - inf_x2) * (sup_y2 - sup_y))
        arie_noua.append((sup_x2 - sup_x) * (inf_y - inf_y2))
        arie_noua.append((inf_x - inf_x2) * (inf_y - inf_y2))

        for ar in arie_noua:
            if ar < arie_minima and ar:
                arie_minima = ar
        print("EXISTA un dreptunghi cu proprietatea ceruta. Valoarea nimina a ariilor dreptunghiurilor cu proprietatea ceruta este", arie_minima)
else:
    print("NU EXISTA un dreptunghi cu proprietatea ceruta.")
