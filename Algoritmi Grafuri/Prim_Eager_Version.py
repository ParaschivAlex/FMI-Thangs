# O(E * log(V))

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
print(N)
IPQ = []

visited = [False for _ in range(N)]

def eagerPrims(start):
    M = N - 1 # numar de muchii din MST
    edgeCount, mstCost = 0, 0
    mstEdges = [None for _ in range(M)]
    relaxEdgesAtNodes(start)

    while len(IPQ) and edgeCount != M:
        dest, fr, to, cst = IPQ.pop(0)
        if visited[to]:
            continue
        mstEdges[edgeCount] = (fr, to , cst)
        edgeCount +=1
        mstCost += cst

        relaxEdgesAtNodes(dest)

    if edgeCount != M:
        return (None, None) # nu exista MST
    return mstCost, mstEdges

def check(x, lst):
    for i in range(len(lst)):
        if lst[i][1] == x:
            return 1
    return 0

def relaxEdgesAtNodes(index):
    visited[index] = True # marcam nodul ca si vizitat

    edges = graph[index]
    for edge in edges: # iteram prin toate muchiile care ies din nodul curent si le adaugam in PQ pe cele care au noduri nevizitate
        destination = edge[1]
        if visited[destination]:
            continue
        if check(destination, IPQ) == 0:
            IPQ.append((destination, edge[0], edge[1], edge[2]))
            IPQ.sort(key=lambda x: x[3])
        else:
            for i in range(len(IPQ)):
                if IPQ[i][0] == destination:
                    index_ipq = i
                    break
            IPQ.pop(index_ipq)
            IPQ.sort(key=lambda x: x[2])

cost, muchii = eagerPrims(0)
print(cost, muchii)