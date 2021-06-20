# Paraschiv Alexandru-Andrei
# Grupa 243

f = open("pb1.txt")

n = int(f.readline())
# print(n)

inf_x, sup_x, inf_y, sup_y = -99999, 99999, -99999, 99999  # valorile care ar trebui sa fie infinit si -infinit
x_neg, x_poz, y_neg, y_poz = 0, 0, 0, 0  # bool pentru a vedea daca am valorile pentru toate inf si sup. Puteam sa testez direct cu inf si sup dar am considerat ca e mai clar.
marginita, intersectie = 0, 0  # 0 -> fals, 1 -> adevarat, 2(doar pt intersectie) -> daca avem un inf==sup
semiplane = []
for i in range(n):  # in citire normalizez si datele si calculez si inf si sup pt x si y.
    a, b, c = f.readline().split()
    semiplane.append([float(a), float(b), float(c)])
    if semiplane[i][1] == 0:  # y == 0
        if semiplane[i][0] < 0:
            semiplane[i][2] = semiplane[i][2] / semiplane[i][0] * (-1)  # calculez in valoarea lui c valoarea pt inf/sup. Schimb valorile definitiv pentru ca nu le mai folosesc
            semiplane[i][0] = -1
            inf_x = max(inf_x, semiplane[i][2])
            x_neg = 1
        else:  # stiu ca am a > 0 altfel, din enunt
            semiplane[i][2] = semiplane[i][2] / semiplane[i][0] * (-1)
            semiplane[i][0] = 1
            sup_x = min(sup_x, semiplane[i][2])
            x_poz = 1
    elif semiplane[i][0] == 0:
        if semiplane[i][1] < 0:
            semiplane[i][2] = semiplane[i][2] / semiplane[i][1] * (-1)
            semiplane[i][1] = -1
            inf_y = max(inf_y, semiplane[i][2])
            y_neg = 1
        else:
            semiplane[i][2] = semiplane[i][2] / semiplane[i][1] * (-1)
            semiplane[i][1] = 1
            sup_y = min(sup_y, semiplane[i][2])
            y_poz = 1

f.close()

if x_neg != 0 and x_poz != 0 and y_neg != 0 and y_poz != 0:
    marginita = 1

# tratez cazul in care mi se da doar un plan si il tratez ca si cum este intersectie vida
if (inf_x == -99999 and sup_x == 99999 and inf_y == -99999) or (inf_x == -99999 and sup_x == 99999 and sup_y == 99999) or (inf_x == -99999 and inf_y == -99999 and sup_y == 99999) or (sup_x == 99999 and inf_y == -99999 and sup_y == 99999):
    intersectie = 0
elif inf_x == sup_x or inf_y == sup_y:  # daca un inf == sup
    intersectie = 2  # caz special
elif inf_x < sup_x and inf_y < sup_y:  # cazul in care am intersectie marginita
    intersectie = 1
elif inf_x > sup_x:  # caut daca am intersectie nemarginita
    if inf_x != -99999 and sup_x != 99999:  # daca inf > sup si una am plan pt ambele (inf si sup) atunci clar e intersectie vida
        intersectie = 0
    elif inf_x == -99999 or sup_x == 99999:  # daca infimum e mai mare ca supremum si nu avem plan pt una dintre ele (adica nu s-a schimbat una dintre ele)
        # (x sau y in functie de caz) atunci avem intersectie nevida si nemarginita
        intersectie = 1
elif inf_y > sup_y:
    if inf_y != -99999 and sup_y != 99999:
        intersectie = 0
    elif inf_y == -99999 or sup_y == 99999:
        intersectie = 1

print("Inf_x, Sup_x, Inf_y, Sup_y  --->   ", inf_x, sup_x, inf_y, sup_y)

print("Intersectie", intersectie)
print("Marginire", marginita)

if intersectie == 1:
    if marginita:
        print("Intersectie NEVIDA si MARGINITA.")
    else:
        print("Intersectie NEVIDA si NEMARGINITA.")
elif intersectie == 0:
    print("Intersectie VIDA")
elif intersectie == 2:
    print("Cel putin 2 limite sunt egale. Exceptie.")
