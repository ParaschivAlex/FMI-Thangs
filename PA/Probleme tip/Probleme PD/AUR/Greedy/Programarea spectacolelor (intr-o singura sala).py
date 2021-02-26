qf = open('spectacole.txt', 'r')
spectacole = []
for linie in f.readlines():
    linie = linie.split()
    spectacole.append((linie[0], linie[1], linie[3]))
spectacole.sort(key = lambda x: x[2])
ora_sfarsit = spectacole[0][2]
nr_maxim_spectacole = 1
solutie = [spectacole[0][0]]
for spectacol in spectacole[1:]:
    ora_inceput = spectacol[1]
    if ora_inceput >= ora_sfarsit:
        nr_maxim_spectacole += 1
        ora_sfarsit = spectacol[2]
        solutie.append(spectacol[0])
print("Numarul maxim de spectacole este %s, fiind programare urmatoarele: " % nr_maxim_spectacole, end = ' ')
for elem in solutie:
    if elem != solutie[len(solutie)-1]:
        print("%s, " % elem, end = '')
    else:
        print("%s." % elem)
f.close()