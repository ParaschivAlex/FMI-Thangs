f = open('monede.txt')
suma = int(f.readline())
bancnote = [int(i) for i in f.readline().split()]
s = 0
nr_bancnote_folosite = 0
solutie = []
i = 0
while i < len(bancnote):
    bancnota_actuala = bancnote[i]
    k = 0
    while s + bancnote[i] <= suma:
        s += bancnote[i]
        k += 1
        nr_bancnote_folosite += 1
    if k != 0:
        solutie.append("%s x %s" % (k, bancnota_actuala))
    i += 1
print("Numarul minim de bancnote folosite este %s, solutia fiind: " % nr_bancnote_folosite, end = ' ')
for elem in solutie:
    if elem != solutie[len(solutie)-1]:
        print("%s, " % elem, end = '')
    else:
        print("%s." % elem, end = ' ')
f.close()