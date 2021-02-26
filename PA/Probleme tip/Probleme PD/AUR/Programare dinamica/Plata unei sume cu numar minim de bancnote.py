f = open('bancnote.txt', 'r')
S = int(f.readline())
v = [int(i) for i in f.readline().split()]
def posibil(i):
    global nrmin, v
    nr_bancnote = float("+inf")
    predecesor = -1
    for j in range(len(v)):
        if i >= v[j]:
            if nrmin[i-v[j]] <= nr_bancnote:
                nr_bancnote = nrmin[i-v[j]]
                predecesor = v[j]
    return nr_bancnote, predecesor

nrmin = [float("+inf") for i in range(S+1)]
pred = [-1 for i in range(S+1)]
nrmin[0] = 0
for i in range(1, S+1):
    nr_bancnote, predecesor = posibil(i)
    if nr_bancnote != float("+inf"):
        nrmin[i] = 1 + nr_bancnote
        pred[i] = predecesor
print(nrmin)
print(pred)
print("Numarul minim de bancnote folosite este %s. Solutie: " % nrmin[S], end = '')

k = S
while k > 0:
    print(pred[k], end = ' ')
    k -= pred[k]

f.close()