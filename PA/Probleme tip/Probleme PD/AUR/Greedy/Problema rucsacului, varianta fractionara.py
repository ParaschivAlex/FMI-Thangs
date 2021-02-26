f = open('rucsac.txt', 'r')
n = int(f.readline())
v = []
for i in range(n):
    linie = f.readline().split()
    v.append(((i+1), int(linie[0]), int(linie[1]), int(linie[0])/int(linie[1])))
G = int(f.readline())
v.sort(key = lambda x: x[3], reverse = True)
obiecte_alese = []
for obiect in v:
    greutate_obiect = obiect[2]
    if greutate_obiect <= G:
        G -= greutate_obiect
        obiecte_alese.append([obiect, 1])
    else:
        fractie = round(G/greutate_obiect, 3)
        obiecte_alese.append([obiect, fractie])
        G = 0
    if G == 0:
        break

profit = 0
print("Obiectele alese sunt: ")
for elem in obiecte_alese:
    print("Obiectul %s - Cantitate %s" % (elem[0][0], elem[1]))
    profit += elem[1] * elem[0][1]
print("Profitul maxim este de %s. " % profit)
f.close()