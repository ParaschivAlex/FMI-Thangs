# O(E * log(E))

""""
Avem un min PQ care sorteaza muchiile dupa cost minim. Astfel, vom determina urmatorul nod care trebuie vizitat si muchia folosita pentru a ajunge acolo.
Incepem algoritmul de la orice nod S. Marcam S ca si vizitat si iteram peste toate muchiile lui S, adaugandu-le in PQ.
Cat timp PQ nu este VIDA si nu am format un MST, scoatem din PQ urmatoarea muchie minima. Daca aceasta are un nod care deja a fost vizitat atunci SKIP si scoatem alta.
Altfel, marcam nodul curent ca si vizitat si adaugam muchia in MST. Iteram peste muchiile noului nod curent si le adaugam in PQ. Nu adaugam muchii are au nod deja vizitat.
"""

graph = [
    [(0, 1, 10), (0, 2, 1), (0, 3, 4)],
    [(1, 0, 10), (1, 2, 3), (1, 4, 0)],
    [(2, 0, 1), (2, 1, 3), (2, 3, 2), (2, 5, 8)],
    [(3, 0, 4), (3, 2, 2), (3, 5, 2), (3, 6, 7)],
    [(4, 1, 0), (4, 5, 1), (4, 7, 8)],
    [(5, 2, 8), (5, 3, 2), (5, 4, 1), (5, 6, 6), (5, 7, 9)],
    [(6, 3, 7), (6, 5, 6), (6, 7, 12)],
    [(7, 4, 8), (7, 5, 9), (7, 6, 12)]
]

N = len(graph)

PQ = []

visited = [False for _ in range(N)]

def lazyPrims(start):
    M = N - 1 # numar de muchii din MST
    edgeCount, mstCost = 0, 0
    mstEdges = [None for _ in range(M)]
    addEdges(start)

    while len(PQ) and edgeCount != M:
        fr, to, cst = PQ.pop(0)
        if visited[to]:
            continue
        mstEdges[edgeCount] = (fr, to , cst)
        edgeCount +=1
        mstCost += cst

        addEdges(to)

    if edgeCount != M:
        return (None, None) # nu exista MST
    return mstCost, mstEdges

def addEdges(index):
    visited[index] = True # marcam nodul ca si vizitat

    edges = graph[index]
    for edge in edges: # iteram prin toate muchiile care ies din nodul curent si le adaugam in PQ pe cele care au noduri nevizitate
        if not visited[edge[1]]:
            PQ.append(edge)
            PQ.sort(key=lambda x: x[2])

cost, muchii = lazyPrims(0)
print(cost, muchii)

