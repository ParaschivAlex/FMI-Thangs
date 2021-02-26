f = open('spectacole_min.txt', 'r')
spectacole = []
for linie in f.readlines():
    linie = linie.split()
    spectacole.append((linie[3], linie[0], linie[2])) # nume, ora_inceput, ora_sfarsit
spectacole.sort(key = lambda x: x[1])
sali = [ [spectacole[0]] ]
k = 1
for spectacol in spectacole[1:]:
    ora_inceput = spectacol[1]
    for i in range (len(sali)):
        ora_sfarsit = sali[i][-1][2]
        if ora_inceput >= ora_sfarsit:
            sali[i].append(spectacol)
            break
    else:
        sali.append([spectacol])
        k += 1
print("Numarul minim de sali necesare este %s, spectacolele alese fiind: " % k)
for i in range(k):
    print("Sala %s : " % (i+1), end = ' ')
    for j in sali[i]:
        print("%s " % j[0], end = '')
    print("\n")
f.close()