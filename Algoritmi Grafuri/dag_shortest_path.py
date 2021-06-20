# Sortarea topologica returneaza o ordonare a nodurilor in asa fel incat niciun nod din lista nu are muchie catre
# un nod care e inaintea lui in lista. Sortarea Topologica merge doar pe grafuri aciclice orientate (DAG - directed acyclic graph)

# Pentru fiecare nod i care are muchie care alt nod j, gasim i inainte lui j in lista din sortarea topologica.
graph = [
    [(1, 3), (2, 6)],
    [(2, 4), (3, 4), (4, 11)],
    [(3, 8), (6, 11)],
    [(4, -4), (5, 5), (6, 2)],
    [(7, 9)],
    [(7, 1)],
    [(7, 2)],
    []
]
print(len(graph))
print(graph)
N = 8


def sortare_topologica(graph, N):
    V = [False for _ in range(N)]  # vectorul de vizitati
    ordering = [0 for _ in range(N)]
    i = N - 1  # indexul pt ordering

    for at in range(N):
        if V[at] == False:
            i = dfs(i, at, V, ordering, graph)
    return ordering


def dfs(i, k, V, ordering, graph):
    V[k] = True

    for edge in graph[k]:
        # print(edge) #V[edge], graph[k])
        if V[edge[0]] == False:
            i = dfs(i, edge[0], V, ordering, graph)
    ordering[i] = k
    return i - 1


sortare = sortare_topologica(graph, N)
# for i in range(len(graph)):
# sortare[i] += 1
print(sortare)


def dagShortestPath(graph, numNodes):
    topsort = sortare_topologica(graph, numNodes)
    dist = [None for _ in range(numNodes)]
    dist[topsort[0]] = 0
    for i in range(numNodes):
        nodeIndex = topsort[i]
        for edge in graph[nodeIndex]:
            newDist = dist[nodeIndex] + edge[1]
            if dist[edge[0]] is None:
                dist[edge[0]] = newDist
            else:
                dist[edge[0]] = min(dist[edge[0]], newDist)
    return dist


dists = dagShortestPath(graph, N)
print(dists)
